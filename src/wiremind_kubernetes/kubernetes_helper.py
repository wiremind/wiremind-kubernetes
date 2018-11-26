# -*- coding: utf-8 -*-
from future.standard_library import install_aliases

install_aliases()

import os

import kubernetes

from .utils import retry_kubernetes_request
from .kube_config import _load_oid_token


class KubernetesHelper(object):
    """
    A simple helper for Kubernetes manipulation.
    """

    deployment_namespace = None
    client_appsv1_api = None
    client_custom_objects_api = None

    def __init__(self, use_kubeconfig=False, deployment_namespace=None):
        """
        :param use_kubeconfig:
            Use ~/.kube/config file to authenticate.
            If false, use kubernetes built-in in_cluster mechanism.
            Defaults to False.
        :param deployment_namespace:
            Target namespace to use.
            If not defined, try to get it from kubernetes built-in serviceAccount mechanism.
        """
        if use_kubeconfig:
            # Fixes https://github.com/kubernetes-client/python-base/issues/65
            kubernetes.config.kube_config.KubeConfigLoader._load_oid_token = _load_oid_token
            kubernetes.config.load_kube_config()
        else:
            kubernetes.config.load_incluster_config()
        self.client_appsv1_api = kubernetes.client.AppsV1Api()
        self.client_custom_objects_api = kubernetes.client.CustomObjectsApi()
        if deployment_namespace:
            self.deployment_namespace = deployment_namespace
        else:
            self.deployment_namespace = open(
                "/var/run/secrets/kubernetes.io/serviceaccount/namespace"
            ).read()

    @retry_kubernetes_request
    def get_deployment_scale(self, deployment_name):
        print("Getting deployment scale for %s" % deployment_name)
        return self.client_appsv1_api.read_namespaced_deployment_scale(
            deployment_name, self.deployment_namespace, pretty="true"
        )

    @retry_kubernetes_request
    def scale_down_deployment(self, deployment_name):
        body = self.get_deployment_scale(deployment_name)
        print("Deleting all Pods for %s" % deployment_name)
        body.spec.replicas = 0
        self.client_appsv1_api.patch_namespaced_deployment_scale(
            deployment_name, self.deployment_namespace, body, pretty="true"
        )

    @retry_kubernetes_request
    def scale_up_deployment(self, deployment_name, pod_amount):
        body = self.get_deployment_scale(deployment_name)
        print("Recreating backend Pods for %s" % deployment_name)
        body.spec.replicas = pod_amount
        self.client_appsv1_api.patch_namespaced_deployment_scale(
            deployment_name, self.deployment_namespace, body, pretty="true"
        )
        print("Done recreating.")

    @retry_kubernetes_request
    def is_deployment_stopped(self, deployment_name):
        print("Asking if deployment %s is stopped" % deployment_name)
        replicas = self.client_appsv1_api.read_namespaced_deployment_scale(
            deployment_name, self.deployment_namespace, pretty="true"
        ).status.replicas
        return replicas == 0

    @retry_kubernetes_request
    def get_deployment_name_to_be_stopped_list(self):
        """
        Return a list of celery or any other deployment that requires
        stop before migration and start after migration.
        """
        print("Getting deployment-to-be-stopped-before-deployment list")
        release_name = os.environ['RELEASE_NAME']
        deployment_list = self.client_appsv1_api.list_namespaced_deployment(
            watch=False,
            label_selector="chartreuse=enabled,release=%s" % release_name,
            namespace=self.deployment_namespace,
        ).items
        deployment_name_list = [
            deployment.metadata.name for deployment in deployment_list
        ]
        print("List is: %s" % deployment_name_list)
        return deployment_name_list

    @retry_kubernetes_request
    def get_expected_deployment_scale_dict(self, release_name=None):
        """
        Return a dict of expected deployment scale

        key: Deployment name
        value: expected Deployment Scale (replicas)
        """
        print("Getting Expected Deployment Scale list")
        if not release_name:
            release_name = os.environ['RELEASE_NAME']
        eds_list = self.client_custom_objects_api.list_namespaced_custom_object(
            namespace=self.deployment_namespace,
            group="wiremind.fr",
            version="v1",
            plural="expecteddeploymentscales",
            label_selector="release=%s" % release_name,
        )
        eds_dict = {
            eds['spec']['deploymentName']: eds['spec']['expectedScale'] for eds in eds_list['items']
        }
        print("List is %s" % eds_dict)
        return eds_dict
