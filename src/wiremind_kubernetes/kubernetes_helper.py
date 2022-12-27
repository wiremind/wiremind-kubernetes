import logging
import pprint
import time
from typing import Any, Dict, Generator, List, Optional, Union

import kubernetes

from wiremind_kubernetes.exceptions import PodNotFound

from .kube_config import load_kubernetes_config
from .kubernetes_client_additional_arguments import (
    AppV1ApiWithArguments,
    AutoscalingV1ApiWithArguments,
    BatchV1ApiWithArguments,
    CoreV1ApiWithArguments,
    CustomObjectsApiWithArguments,
    RbacAuthorizationV1ApiWithArguments,
)
from .utils import retry_kubernetes_request, retry_kubernetes_request_no_ignore

logger = logging.getLogger(__name__)

HPA_ID_PREFIX = "wm--disabled--kube"


class KubernetesHelper:
    """
    A simple helper for Kubernetes manipulation.
    """

    SCALE_DOWN_MAX_WAIT_TIME = 3600

    def __init__(
        self,
        use_kubeconfig: bool = False,
        dry_run: bool = False,
        should_load_kubernetes_config: bool = True,
        context: Optional[str] = None,
    ):
        """
        :param use_kubeconfig:
            Use ~/.kube/config file to authenticate.
            If false, use kubernetes built-in in_cluster mechanism.
            Defaults to False.
        :param dry_run:
            Dry run.
        :param should_load_kubernetes_config:
            if true, will call load_kubernetes_config(use_kubeconfig)
            Defaults to True.
        """
        if should_load_kubernetes_config:
            load_kubernetes_config(use_kubeconfig=use_kubeconfig, context=context)
        self.client_corev1_api: kubernetes.client.CoreV1Api = CoreV1ApiWithArguments(dry_run=dry_run)
        self.client_appsv1_api: kubernetes.client.AppsV1Api = AppV1ApiWithArguments(dry_run=dry_run)
        self.client_batchv1_api: kubernetes.client.BatchV1Api = BatchV1ApiWithArguments(dry_run=dry_run)
        self.client_autoscalingv1_api: kubernetes.client.AutoscalingV1Api = AutoscalingV1ApiWithArguments(
            dry_run=dry_run
        )
        self.client_custom_objects_api: kubernetes.client.CustomObjectsApi = CustomObjectsApiWithArguments(
            dry_run=dry_run
        )
        self.client_rbac_authorization_v1_api: kubernetes.client.RbacAuthorizationV1Api = (
            RbacAuthorizationV1ApiWithArguments(dry_run=dry_run)
        )

        self.dry_run: bool = dry_run


def _get_namespace_from_kube() -> str:
    return open("/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()


class NamespacedKubernetesHelper(KubernetesHelper):
    """
    A simple helper for Kubernetes manipulation.
    """

    def __init__(
        self,
        use_kubeconfig: bool = False,
        namespace: Union[None, str] = None,
        dry_run: bool = False,
        should_load_kubernetes_config: bool = True,
        context: Optional[str] = None,
    ):
        """
        :param use_kubeconfig:
            Use ~/.kube/config file to authenticate.
            If false, use kubernetes built-in in_cluster mechanism.
            Defaults to False.
        :param namespace:
            Target namespace to use.
            If not defined, try to get it from kubernetes built-in serviceAccount mechanism.
        :param dry_run:
            Dry run.
        """
        super().__init__(
            use_kubeconfig=use_kubeconfig,
            dry_run=dry_run,
            should_load_kubernetes_config=should_load_kubernetes_config,
            context=context,
        )
        if namespace:
            self.namespace = namespace
        else:
            self.namespace = _get_namespace_from_kube()

    def get_deployment_scale(self, deployment_name: str) -> kubernetes.client.V1Scale:
        logger.debug("Getting deployment scale for %s", deployment_name)
        return self.client_appsv1_api.read_namespaced_deployment_scale(deployment_name, self.namespace)

    def get_statefulset_scale(self, statefulset_name: str) -> kubernetes.client.V1Scale:
        logger.debug("Getting statefulset scale for %s", statefulset_name)
        return self.client_appsv1_api.read_namespaced_stateful_set_scale(statefulset_name, self.namespace)

    def scale_down_statefulset(self, statefulset_name: str) -> None:
        body = self.get_statefulset_scale(statefulset_name)
        logger.debug("Deleting all Pods for %s", statefulset_name)
        body.spec.replicas = 0
        self.client_appsv1_api.patch_namespaced_stateful_set_scale(statefulset_name, self.namespace, body)
        logger.debug("Done deleting.")

    @retry_kubernetes_request_no_ignore
    def scale_down_deployment(self, deployment_name: str) -> None:
        body = self.get_deployment_scale(deployment_name)
        logger.debug("Deleting all Pods for %s", deployment_name)
        body.spec.replicas = 0
        self.client_appsv1_api.patch_namespaced_deployment_scale(deployment_name, self.namespace, body)
        logger.debug("Done deleting.")

    def scale_up_statefulset(self, statefulset_name: str, pod_amount: int = 1) -> None:
        body = self.get_statefulset_scale(statefulset_name)
        logger.debug("Recreating backend Pods for %s", statefulset_name)
        body.spec.replicas = pod_amount
        self.client_appsv1_api.patch_namespaced_stateful_set_scale(statefulset_name, self.namespace, body)
        logger.debug("Done recreating.")

    @retry_kubernetes_request_no_ignore
    def scale_up_deployment(self, deployment_name: str, pod_amount: int) -> None:
        body = self.get_deployment_scale(deployment_name)
        logger.debug("Recreating backend Pods for %s", deployment_name)
        body.spec.replicas = pod_amount
        self.client_appsv1_api.patch_namespaced_deployment_scale(deployment_name, self.namespace, body)
        logger.debug("Done recreating.")

    def is_statefulset_stopped(self, deployment_name: str) -> bool:
        return self.is_deployment_stopped(deployment_name, statefulset=True)

    @retry_kubernetes_request_no_ignore
    def _get_pods_from_deployment(self, deployment_name: str, statefulset: bool = False) -> List:
        if statefulset:
            logger.debug("Asking if StatefulSet %s is stopped", deployment_name)
            labels = self.client_appsv1_api.read_namespaced_stateful_set(
                deployment_name, self.namespace
            ).spec.selector.match_labels
        else:
            logger.debug("Asking if Deployment %s is stopped", deployment_name)
            labels = self.client_appsv1_api.read_namespaced_deployment(
                deployment_name, self.namespace
            ).spec.selector.match_labels

        try:
            return self.client_corev1_api.list_namespaced_pod(
                namespace=self.namespace, label_selector=",".join(["%s=%s" % kv for kv in labels.items()])
            ).items
        except kubernetes.client.rest.ApiException as e:
            if e.status == 404:
                return []
            else:
                raise

    def is_deployment_stopped(self, deployment_name: str, statefulset: bool = False) -> bool:
        pod_list: List = self._get_pods_from_deployment(deployment_name, statefulset)

        current_scale = 0
        for pod in pod_list:
            if pod.status.phase not in ("Failed"):
                current_scale += 1

        if current_scale > 0:
            kind = statefulset and "StatefulSet" or "Deployment"
            logger.info("%s %s has %s living replicas", deployment_name, kind, current_scale)
            return False
        return True

    def is_deployment_ready(self, deployment_name: str, statefulset: bool = False) -> bool:
        if statefulset:
            status = self.client_appsv1_api.read_namespaced_stateful_set_status(deployment_name, self.namespace)
        else:
            status = self.client_appsv1_api.read_namespaced_deployment_status(deployment_name, self.namespace)
        expected_replicas = status.spec.replicas
        ready_replicas = status.status.ready_replicas
        resource_type = statefulset and "StatefulSet" or "Deployment"
        logger.debug(
            "%s %s has %s expected replicas and %s ready replicas",
            resource_type,
            deployment_name,
            expected_replicas,
            ready_replicas,
        )
        if expected_replicas == 0:
            return True
        return expected_replicas == ready_replicas

    @retry_kubernetes_request
    def getPodNameFromDeployment(self, deployment_name: str, namespace_name: str) -> str:
        """
        From a given deployment, get the first pod name
        """
        try:
            deployment = self.client_appsv1_api.read_namespaced_deployment(deployment_name, namespace_name)
        except kubernetes.client.rest.ApiException as e:
            if e.status == 404:
                raise PodNotFound(f"No deployment {deployment_name} was found in the namespace {namespace_name}")
            else:
                raise
        selector = ",".join(f"{key}={value}" for key, value in deployment.spec.selector.match_labels.items())
        pod_list = self.client_corev1_api.list_namespaced_pod(namespace_name, label_selector=selector).items
        if not pod_list:
            raise PodNotFound("No matching pod was found in the namespace %s" % (namespace_name))
        return pod_list[0].metadata.name

    def get_deployment_hpa(self, *, deployment_name: str) -> Generator:
        for hpa in self.client_autoscalingv1_api.list_namespaced_horizontal_pod_autoscaler(self.namespace).items:
            if hpa.spec.scale_target_ref.kind == "Deployment" and hpa.spec.scale_target_ref.name == deployment_name:
                yield hpa

    def patch_deployment_hpa(self, *, hpa_name: str, body: Any) -> None:
        self.client_autoscalingv1_api.patch_namespaced_horizontal_pod_autoscaler(
            name=hpa_name, namespace=self.namespace, body=body
        )


class KubernetesDeploymentManager(NamespacedKubernetesHelper):
    """
    Subclass of Kubernetes Helper allowing to scale down/up all pods that
    should be stopped/started when doing database migration/maintenance
    (alembic, dump, etc).
    The associated Deployment should define an eds.

    Usage:
    a = wiremind_kubernetes.KubernetesDeploymentManager(use_kubeconfig=True, namespace="my-namespace")
    a.stop_pods()
    do_something('wololo')
    a.start_pods()
    """

    def __init__(self, release_name: str, **kwargs: Any):
        self.release_name = release_name
        super().__init__(**kwargs)

    @retry_kubernetes_request_no_ignore
    def _get_expected_deployment_scale_dict(self) -> Dict[int, Dict[str, int]]:
        """
        Return a dict of expected deployment scale:
        {
            0: {  # priority
                # key: Deployment name, only if it has an associated eds
                # value: expected Deployment Scale (replicas)
                "my-deployment": 3,
                "my-other-deployment": 42
            },
            1: {
                "my-third-deployment": 17,
            },
        }
        """
        logger.debug("Getting Expected Deployment Scale list")
        eds_list: List[Dict[str, Any]] = []
        release_label_keys = ["app.kubernetes.io/instance", "release"]

        for release_label_key in release_label_keys:
            logger.debug(f"Getting Expected Deployment Scale list with the" f" release label key {release_label_key}")
            try:
                eds_list.extend(
                    self.client_custom_objects_api.list_namespaced_custom_object(
                        namespace=self.namespace,
                        group="wiremind.io",
                        version="v1",
                        plural="expecteddeploymentscales",
                        label_selector=f"{release_label_key}={self.release_name}",
                    )["items"]
                )
            except kubernetes.client.rest.ApiException as e:
                if e.status != 404:
                    raise

        eds_dict: Dict[int, Dict[str, int]] = {}
        for eds in eds_list:
            deployment_name: str = eds["spec"]["deploymentName"]
            expected_scale: int = eds["spec"]["expectedScale"]
            # Note: default should be removed once we use CRD v1 with default within the CRD itself
            priority: int = eds["spec"].get("priority", 0)

            if priority not in eds_dict:
                eds_dict[priority] = {}

            eds_dict[priority][deployment_name] = expected_scale

        logger.debug("Deployments are %s", pprint.pformat(eds_dict))
        return eds_dict

    def start_pods(self) -> None:
        """
        Start all Pods that should be started
        """
        expected_deployment_scale_dict: Dict[int, Dict[str, int]] = self._get_expected_deployment_scale_dict()

        logger.info("Scaling up application Deployments...")
        if not expected_deployment_scale_dict:
            logger.info("No Deployments to scale up")
            return

        priority_dict: Dict[str, int]
        # Don't assume anything about having a priority dict within the main dict
        # So we manually test for existence
        scaled: bool = False
        for priority_dict in expected_deployment_scale_dict.values():
            name: str
            expected_scale: int
            if len(priority_dict):
                scaled = True
                for (name, expected_scale) in priority_dict.items():
                    self.re_enable_hpa(deployment_name=name)
                    self.scale_up_deployment(name, expected_scale)
        if scaled:
            logger.info("Done scaling up application Deployments")
        else:
            logger.info("No Deployments to scale up")

    def _are_deployments_stopped(self, deployment_dict: Dict[str, int]) -> bool:
        for deployment_name in deployment_dict:
            if not self.is_deployment_stopped(deployment_name):
                return False
        return True

    @retry_kubernetes_request
    def disable_hpa(self, *, deployment_name: str) -> None:
        for hpa in self.get_deployment_hpa(deployment_name=deployment_name):
            # Tell the hpa to manage a non-existing Deployment
            hpa.spec.scale_target_ref.name = f"{HPA_ID_PREFIX}-{deployment_name}"
            self.patch_deployment_hpa(hpa_name=hpa.metadata.name, body=hpa)

    @retry_kubernetes_request
    def re_enable_hpa(self, *, deployment_name: str) -> None:
        for hpa in self.get_deployment_hpa(deployment_name=f"{HPA_ID_PREFIX}-{deployment_name}"):
            hpa.spec.scale_target_ref.name = deployment_name
            self.patch_deployment_hpa(hpa_name=hpa.metadata.name, body=hpa)

    def _stop_deployments(self, deployment_dict: Dict[str, int]) -> None:
        """
        Scale down a dict (deployment_name, expected_scale) of Deployments.
        """
        for _ in range(self.SCALE_DOWN_MAX_WAIT_TIME):
            for deployment_name in deployment_dict:
                self.disable_hpa(deployment_name=deployment_name)
                self.scale_down_deployment(deployment_name)
            if self._are_deployments_stopped(deployment_dict):
                break
            time.sleep(1)
        else:
            raise Exception("Timed out waiting for pods to be deleted: aborting.")

    def stop_pods(self) -> None:
        """
        Scale to 0 all deployments for which an ExpectedDeploymentScale links to.
        stop all deployments, then wait for actual stop, by priority (descending order):
        Example: stop all deployments with priority 1, then all deployments with priority 0
        """
        expected_deployment_scale_dict: Dict[int, Dict[str, int]] = self._get_expected_deployment_scale_dict()

        logger.info("Scaling down application Deployments...")
        if not expected_deployment_scale_dict:
            logger.info("No Deployments to scale down")
            return

        priority: int
        priorities: List[int] = sorted(expected_deployment_scale_dict, reverse=True)
        for priority in priorities:
            priority_dict: Dict[str, int] = expected_deployment_scale_dict[priority]
            if len(priority_dict):
                self._stop_deployments(priority_dict)
        logger.info("Done scaling down application Deployments.")

    def generate_job(
        self,
        job_name: str,
        container_image: str,
        labels: Dict[str, str],
        command: Union[str, None] = None,
        args: Union[List[str], None] = None,
        environment_variables: Union[Dict["str", "str"], None] = None,
        ttl_seconds_after_finished: int = 1800,
        image_pull_secrets: Union[List[kubernetes.client.V1LocalObjectReference], None] = None,
        image_pull_policy: str = "IfNotPresent",
        priority_class_name: str = "",
    ) -> kubernetes.client.V1Job:
        """
        Generate a job object.
        Note that label is mandatory since everything created in the cluster should have labels
        allowing for automatic deletion or garbage collection.
        """
        job_name = f"{self.release_name}-{job_name}"
        if environment_variables is None:
            environment_variables = {}

        job = kubernetes.client.V1Job(api_version="batch/v1", kind="Job")

        job_metadata = kubernetes.client.V1ObjectMeta(namespace=self.namespace, name=job_name)
        job_metadata.labels = labels
        job.metadata = job_metadata

        job.status = kubernetes.client.V1JobStatus()

        container = kubernetes.client.V1Container(
            name="wiremind", image=container_image, image_pull_policy=image_pull_policy
        )
        if command:
            container.command = [command]
        if args:
            container.args = args
        env_list = []
        for env_name, env_value in environment_variables.items():
            env_list.append(kubernetes.client.V1EnvVar(name=env_name, value=env_value))
        container.env = env_list

        pod_template_spec = kubernetes.client.V1PodTemplateSpec()
        pod_template_spec.spec = kubernetes.client.V1PodSpec(
            containers=[container],
            restart_policy="Never",
            image_pull_secrets=image_pull_secrets,
            priority_class_name=priority_class_name,
        )
        pod_template_spec.metadata = kubernetes.client.V1ObjectMeta(labels=labels)

        job.spec = kubernetes.client.V1JobSpec(
            ttl_seconds_after_finished=ttl_seconds_after_finished,
            template=pod_template_spec,
        )

        return job

    def create_job(self, job_body: kubernetes.client.V1Job) -> kubernetes.client.V1Job:
        try:
            return self.client_batchv1_api.create_namespaced_job(self.namespace, job_body)
        except kubernetes.client.rest.ApiException as e:
            print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)

    def get_job(self, job_name: str) -> kubernetes.client.V1Job:
        """
        Get a job, concatenating release_name and job_name as job name.
        """
        job_name = f"{self.release_name}-{job_name}"
        return self.client_batchv1_api.read_namespaced_job(job_name, self.namespace)

    def delete_job(self, job_name: str) -> kubernetes.client.V1Status:
        """
        Get a job, concatenating release_name and job_name as job name.
        """
        job_name = f"{self.release_name}-{job_name}"
        body = kubernetes.client.V1DeleteOptions(propagation_policy="Background")
        return self.client_batchv1_api.delete_namespaced_job(name=job_name, namespace=self.namespace, body=body)
