import logging
import time
from typing import Any, Dict, List, Union

import kubernetes

from wiremind_kubernetes.exceptions import PodNotFound

from .kube_config import load_kubernetes_config
from .utils import retry_kubernetes_request

logger = logging.getLogger(__name__)


class KubernetesHelper:
    """
    A simple helper for Kubernetes manipulation.
    """

    def __init__(
        self, use_kubeconfig: bool = False, dry_run: bool = False, should_load_kubernetes_config: bool = True,
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
            load_kubernetes_config(use_kubeconfig=use_kubeconfig)
        self.client_appsv1_api: kubernetes.client.AppsV1Api = kubernetes.client.AppsV1Api()
        self.client_corev1_api: kubernetes.client.CoreV1Api = kubernetes.client.CoreV1Api()
        self.client_batchv1_api: kubernetes.client.BatchV1Api = kubernetes.client.BatchV1Api()
        self.client_custom_objects_api: kubernetes.client.CustomObjectsApi = kubernetes.client.CustomObjectsApi()

        self.dry_run: bool = dry_run

        # Every read request have those arguments added
        self.read_additional_arguments: Dict[str, Any] = dict(pretty=True)
        # Every request, either read or write, have those arguments added
        self.additional_arguments: Dict[str, Any] = self.read_additional_arguments.copy()
        if dry_run:
            # Dry run, in kube API, is not true or false, but either dry_run: All or not defined.
            self.additional_arguments["dry_run"] = "All"

    def delete_resource(self, resource_name: str, resource_namespace: str, delete_function):
        return delete_function(resource_name, resource_namespace, **self.additional_arguments)

    def delete_pod(self, pod_name: str, pod_namespace: str):
        return self.delete_resource(pod_name, pod_namespace, self.client_corev1_api.delete_namespaced_pod)

    def delete_pvc(self, pvc_name: str, pvc_namespace: str):
        return self.delete_resource(
            pvc_name, pvc_namespace, self.client_corev1_api.delete_namespaced_persistent_volume_claim,
        )

    def delete_job(self, job_name: str, job_namespace: str):
        return self.delete_resource(job_name, job_namespace, self.client_batchv1_api.delete_namespaced_job)

    def delete_secret(self, secret_name: str, secret_namespace: str):
        return self.delete_resource(secret_name, secret_namespace, self.client_corev1_api.delete_namespaced_secret,)

    def delete_deployment(self, deployment_name: str, namespace: str):
        return self.delete_resource(deployment_name, namespace, self.client_appsv1_api.delete_namespaced_deployment,)

    def list_deployment(self, **kwargs):
        return self.client_appsv1_api.list_deployment_for_all_namespaces(**kwargs, **self.read_additional_arguments)

    def list_pod(self, **kwargs):
        return self.client_corev1_api.list_pod_for_all_namespaces(**kwargs, **self.read_additional_arguments)

    def list_pvc(self, **kwargs):
        return self.client_corev1_api.list_persistent_volume_claim_for_all_namespaces(
            **kwargs, **self.read_additional_arguments
        )

    def list_job(self, **kwargs):
        return self.client_batchv1_api.list_job_for_all_namespaces(**kwargs, **self.read_additional_arguments)

    def list_secret(self, **kwargs):
        return self.client_corev1_api.list_secret_for_all_namespaces(**kwargs, **self.read_additional_arguments)


def _get_namespace_from_kube() -> str:
    return open("/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()


class NamespacedKubernetesHelper(KubernetesHelper):
    """
    A simple helper for Kubernetes manipulation.
    """

    def __init__(
        self, use_kubeconfig: bool = False, namespace: Union[None, str] = None, dry_run: bool = False,
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
        super().__init__(use_kubeconfig, dry_run)
        if namespace:
            self.namespace = namespace
        else:
            self.namespace = _get_namespace_from_kube()

    def get_deployment_scale(self, deployment_name: str):
        logger.debug("Getting deployment scale for %s", deployment_name)
        return self.client_appsv1_api.read_namespaced_deployment_scale(
            deployment_name, self.namespace, **self.read_additional_arguments
        )

    def get_statefulset_scale(self, statefulset_name: str):
        logger.debug("Getting statefulset scale for %s", statefulset_name)
        return self.client_appsv1_api.read_namespaced_stateful_set_scale(
            statefulset_name, self.namespace, **self.read_additional_arguments,
        )

    def scale_down_statefulset(self, statefulset_name: str):
        body = self.get_statefulset_scale(statefulset_name)
        logger.debug("Deleting all Pods for %s", statefulset_name)
        body.spec.replicas = 0
        self.client_appsv1_api.patch_namespaced_stateful_set_scale(
            statefulset_name, self.namespace, body, **self.additional_arguments,
        )
        logger.debug("Done deleting.")

    @retry_kubernetes_request
    def scale_down_deployment(self, deployment_name: str):
        body = self.get_deployment_scale(deployment_name)
        logger.debug("Deleting all Pods for %s", deployment_name)
        body.spec.replicas = 0
        self.client_appsv1_api.patch_namespaced_deployment_scale(
            deployment_name, self.namespace, body, **self.additional_arguments,
        )
        logger.debug("Done deleting.")

    def scale_up_statefulset(self, statefulset_name: str, pod_amount: int = 1):
        body = self.get_statefulset_scale(statefulset_name)
        logger.debug("Recreating backend Pods for %s", statefulset_name)
        body.spec.replicas = pod_amount
        self.client_appsv1_api.patch_namespaced_stateful_set_scale(
            statefulset_name, self.namespace, body, **self.additional_arguments,
        )
        logger.debug("Done recreating.")

    @retry_kubernetes_request
    def scale_up_deployment(self, deployment_name: str, pod_amount: int):
        body = self.get_deployment_scale(deployment_name)
        logger.debug("Recreating backend Pods for %s", deployment_name)
        body.spec.replicas = pod_amount
        self.client_appsv1_api.patch_namespaced_deployment_scale(
            deployment_name, self.namespace, body, **self.additional_arguments,
        )
        logger.debug("Done recreating.")

    def is_statefulset_stopped(self, deployment_name: str):
        return self.is_deployment_stopped(deployment_name, statefulset=True)

    @retry_kubernetes_request
    def is_deployment_stopped(self, deployment_name: str, statefulset: bool = False):
        logger.debug("Asking if deployment %s is stopped", deployment_name)
        if statefulset:
            scale = self.client_appsv1_api.read_namespaced_stateful_set_scale(
                deployment_name, self.namespace, **self.read_additional_arguments,
            )
        else:
            scale = self.client_appsv1_api.read_namespaced_deployment_scale(
                deployment_name, self.namespace, **self.read_additional_arguments,
            )
        logger.debug("%s has %s replicas", deployment_name, scale.status.replicas)
        return (scale.status.replicas == 0) or self.dry_run

    def is_deployment_ready(self, deployment_name: str, statefulset: bool = False):
        if statefulset:
            status = self.client_appsv1_api.read_namespaced_stateful_set_status(
                deployment_name, self.namespace, **self.read_additional_arguments,
            )
        else:
            status = self.client_appsv1_api.read_namespaced_deployment_status(
                deployment_name, self.namespace, **self.read_additional_arguments,
            )
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
    def getPodNameFromDeployment(self, deployment_name, namespace_name):
        """
        From a given deployment, get the first pod name
        """
        try:
            deployment = self.client_appsv1_api.read_namespaced_deployment(deployment_name, namespace_name)
        except kubernetes.client.rest.ApiException as e:
            if e.status == 404:
                raise PodNotFound("No deployment %s was found in the namespace %s" % (deployment_name, namespace_name))
            else:
                raise
        selector = ",".join("%s=%s" % (key, value) for key, value in deployment.spec.selector.match_labels.items())
        pod_list = self.client_corev1_api.list_namespaced_pod(namespace_name, label_selector=selector).items
        if not pod_list:
            raise PodNotFound("No matching pod was found in the namespace %s" % (namespace_name))
        return pod_list[0].metadata.name


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

    def __init__(self, release_name: str, **kwargs):
        self.release_name = release_name
        super().__init__(**kwargs)

    def start_pods(self):
        """
        Start all Pods that should be started
        """
        expected_deployment_scale_dict = self._get_expected_deployment_scale_dict()

        if not expected_deployment_scale_dict:
            return

        logger.info("Scaling up application Deployments...")
        for (name, amount) in expected_deployment_scale_dict.items():
            self.scale_up_deployment(name, amount)
        logger.info("Done scaling up application Deployments.")

    def stop_pods(self):
        """
        SQL migration implies that every backend pod should be restarted.
        We stop them before applying migration
        """
        expected_deployment_scale_dict = self._get_expected_deployment_scale_dict()

        if not expected_deployment_scale_dict:
            return

        logger.info("Scaling down application Deployments...")
        for deployment_name in expected_deployment_scale_dict.keys():
            self.scale_down_deployment(deployment_name)

        # Make sure to wait for actual stop (can be looong)
        for _ in range(360):  # 1 hour
            time.sleep(1)
            stopped = 0
            for deployment_name in expected_deployment_scale_dict.keys():
                if self.is_deployment_stopped(deployment_name):
                    stopped += 1
            if stopped == len(expected_deployment_scale_dict):
                break
            else:
                logger.info("All pods not deleted yet. Waiting...")
        logger.info("Done scaling down application Deployments, all Pods have been deleted.")

    @retry_kubernetes_request
    def _get_expected_deployment_scale_dict(self):
        """
        Return a dict of expected deployment scale

        key: Deployment name, only if it has an associated eds
        value: expected Deployment Scale (replicas)
        """
        logger.debug("Getting Expected Deployment Scale list")
        if not self.release_name:
            eds_list = self.client_custom_objects_api.list_namespaced_custom_object(
                namespace=self.namespace, group="wiremind.fr", version="v1", plural="expecteddeploymentscales",
            )
        else:
            eds_list = self.client_custom_objects_api.list_namespaced_custom_object(
                namespace=self.namespace,
                group="wiremind.fr",
                version="v1",
                plural="expecteddeploymentscales",
                label_selector="release=%s" % self.release_name,
            )
            # Support new-style labels as well
            additional_eds_list = self.client_custom_objects_api.list_namespaced_custom_object(
                namespace=self.namespace,
                group="wiremind.fr",
                version="v1",
                plural="expecteddeploymentscales",
                label_selector="app.kubernetes.io/instance=%s" % self.release_name,
            )
            eds_list["items"].extend(additional_eds_list["items"])
        eds_dict = {eds["spec"]["deploymentName"]: eds["spec"]["expectedScale"] for eds in eds_list["items"]}
        logger.debug("List is %s", eds_dict)
        return eds_dict

    def generate_job(
        self,
        job_name: str,
        container_image: str,
        labels: Dict[str, str],
        command: Union[str, None] = None,
        args: Union[List[str], None] = None,
        environment_variables: Union[Dict["str", "str"], None] = None,
        ttl_seconds_after_finished: int = 1800,
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

        container = kubernetes.client.V1Container(name="wiremind", image=container_image)
        if command:
            container.command = [command]
        if args:
            container.args = args
        env_list = []
        for env_name, env_value in environment_variables.items():
            env_list.append(kubernetes.client.V1EnvVar(name=env_name, value=env_value))
        container.env = env_list

        pod_template_spec = kubernetes.client.V1PodTemplateSpec()
        pod_template_spec.spec = kubernetes.client.V1PodSpec(containers=[container], restart_policy="Never")

        job.spec = kubernetes.client.V1JobSpec(
            ttl_seconds_after_finished=ttl_seconds_after_finished, template=pod_template_spec,
        )

        return job

    def create_job(self, job_body: kubernetes.client.V1Job) -> kubernetes.client.V1Job:
        try:
            return self.client_batchv1_api.create_namespaced_job(self.namespace, job_body, **self.additional_arguments)
        except kubernetes.client.rest.ApiException as e:
            print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)
