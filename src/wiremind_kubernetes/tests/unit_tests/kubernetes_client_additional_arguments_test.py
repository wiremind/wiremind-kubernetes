import kubernetes.client
import pytest
from pytest_mock import MockerFixture

import wiremind_kubernetes.kubernetes_helper


def test_kubernetes_client_additional_arguments_core_v1_api(
    mocker: MockerFixture,
) -> None:
    """
    Test that we add mandatory args to each function call of kubernetes client
    """
    mocked_read_namespaced_pod = mocker.patch("kubernetes.client.CoreV1Api.read_namespaced_pod")
    mocked_create_namespaced_pod = mocker.patch("kubernetes.client.CoreV1Api.create_namespaced_pod")

    kubernetes_helper = wiremind_kubernetes.kubernetes_helper.KubernetesHelper(
        dry_run=True, should_load_kubernetes_config=False
    )

    pod = kubernetes.client.V1Pod()
    kubernetes_helper.client_corev1_api.read_namespaced_pod("foo", "bar")
    mocked_read_namespaced_pod.assert_called_once_with("foo", "bar", pretty="true")

    kubernetes_helper.client_corev1_api.create_namespaced_pod("foo", pod)
    mocked_create_namespaced_pod.assert_called_once_with("foo", pod, pretty="true", dry_run="All")


def test_kubernetes_client_additional_arguments_disabled_core_v1_api(
    mocker: MockerFixture,
) -> None:
    """
    Test that we do not add args to each function call of kubernetes client
    """
    mocked_read_namespaced_pod = mocker.patch("kubernetes.client.CoreV1Api.read_namespaced_pod")
    mocked_create_namespaced_pod = mocker.patch("kubernetes.client.CoreV1Api.create_namespaced_pod")

    kubernetes_helper = wiremind_kubernetes.kubernetes_helper.KubernetesHelper(
        dry_run=True, pretty=False, should_load_kubernetes_config=False
    )

    pod = kubernetes.client.V1Pod()
    kubernetes_helper.client_corev1_api.read_namespaced_pod("foo", "bar")
    mocked_read_namespaced_pod.assert_called_once_with("foo", "bar")

    kubernetes_helper.client_corev1_api.create_namespaced_pod("foo", pod)
    mocked_create_namespaced_pod.assert_called_once_with("foo", pod, dry_run="All")


@pytest.mark.parametrize(
    "method_name,args",
    [
        ("get_api_resources", ("group", "version")),
        ("get_cluster_custom_object", ("group", "version", "plural", "name")),
        ("get_cluster_custom_object_scale", ("group", "version", "plural", "name")),
        ("get_cluster_custom_object_status", ("group", "version", "plural", "name")),
        (
            "get_namespaced_custom_object",
            ("group", "version", "namespace", "plural", "name"),
        ),
        (
            "get_namespaced_custom_object_scale",
            ("group", "version", "namespace", "plural", "name"),
        ),
        (
            "get_namespaced_custom_object_status",
            ("group", "version", "namespace", "plural", "name"),
        ),
    ],
)
def test_custom_objects_read_methods_skip_pretty(
    mocker: MockerFixture, method_name: str, args: tuple[str, ...]
) -> None:
    # These generated read methods raise ApiTypeError if `pretty` is forwarded.
    mocked_method = mocker.patch(f"kubernetes.client.CustomObjectsApi.{method_name}")

    kubernetes_helper = wiremind_kubernetes.kubernetes_helper.KubernetesHelper(
        dry_run=True, should_load_kubernetes_config=False
    )

    getattr(kubernetes_helper.client_custom_objects_api, method_name)(*args)

    mocked_method.assert_called_once_with(*args)


def test_custom_objects_list_methods_keep_pretty(mocker: MockerFixture) -> None:
    # Keep the shared pretty behavior on list methods that still accept it.
    mocked_list_cluster_custom_object = mocker.patch("kubernetes.client.CustomObjectsApi.list_cluster_custom_object")

    kubernetes_helper = wiremind_kubernetes.kubernetes_helper.KubernetesHelper(
        dry_run=True, should_load_kubernetes_config=False
    )

    kubernetes_helper.client_custom_objects_api.list_cluster_custom_object("group", "version", "plural")

    mocked_list_cluster_custom_object.assert_called_once_with("group", "version", "plural", pretty="true")


class RequestSent(Exception):
    pass


def test_pretty_passes_generated_client_validation(mocker: MockerFixture) -> None:
    # Call the real generated methods: kubernetes>=37 validates `pretty` as a string before it sends the request.
    mocker.patch("kubernetes.client.ApiClient.call_api", side_effect=RequestSent)

    kubernetes_helper = wiremind_kubernetes.kubernetes_helper.KubernetesHelper(
        dry_run=True, should_load_kubernetes_config=False
    )

    with pytest.raises(RequestSent):
        kubernetes_helper.client_corev1_api.read_namespace("foo")
    with pytest.raises(RequestSent):
        kubernetes_helper.client_corev1_api.create_namespaced_pod("foo", kubernetes.client.V1Pod())
