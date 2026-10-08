import inspect
from collections.abc import Callable

import kubernetes.client
import pytest
from pytest_mock import MockerFixture

import wiremind_kubernetes.kubernetes_helper
from wiremind_kubernetes.kubernetes_client_additional_arguments import (
    AdmissionregistrationV1ApiWithArguments,
    AppV1ApiWithArguments,
    AutoscalingV1ApiWithArguments,
    AutoscalingV2ApiWithArguments,
    BatchV1ApiWithArguments,
    ClientWithArguments,
    CoreV1ApiWithArguments,
    CustomObjectsApiWithArguments,
    NetworkingV1ApiWithArguments,
    RbacAuthorizationV1ApiWithArguments,
    StorageV1ApiWithArguments,
)


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


def test_custom_objects_write_methods_skip_pretty(mocker: MockerFixture) -> None:
    # Custom object patch, replace and delete methods accept dry_run but not pretty.
    mocked_patch = mocker.patch("kubernetes.client.CustomObjectsApi.patch_namespaced_custom_object")

    kubernetes_helper = wiremind_kubernetes.kubernetes_helper.KubernetesHelper(
        dry_run=True, should_load_kubernetes_config=False
    )

    kubernetes_helper.client_custom_objects_api.patch_namespaced_custom_object(
        "group", "version", "namespace", "plural", "name", {}
    )

    mocked_patch.assert_called_once_with("group", "version", "namespace", "plural", "name", {}, dry_run="All")


@pytest.mark.parametrize(
    "wrapper_class",
    [
        AdmissionregistrationV1ApiWithArguments,
        AppV1ApiWithArguments,
        AutoscalingV1ApiWithArguments,
        AutoscalingV2ApiWithArguments,
        BatchV1ApiWithArguments,
        CoreV1ApiWithArguments,
        CustomObjectsApiWithArguments,
        NetworkingV1ApiWithArguments,
        RbacAuthorizationV1ApiWithArguments,
        StorageV1ApiWithArguments,
    ],
)
def test_additional_arguments_are_method_parameters(wrapper_class: Callable[..., ClientWithArguments]) -> None:
    # Each generated method must accept every argument that the wrapper adds to its calls.
    wrapper = wrapper_class(dry_run=True, pretty=True)
    for method_name, method in inspect.getmembers(wrapper.client, inspect.ismethod):
        if method_name.startswith("_"):
            continue
        parameters = inspect.signature(method).parameters
        if any(parameter.kind is inspect.Parameter.VAR_KEYWORD for parameter in parameters.values()):
            pytest.skip("kubernetes<37 hides the method parameters in **kwargs")
        assert set(wrapper.get_additional_arguments(method_name)) <= set(parameters), method_name
