from pytest_mock import MockerFixture

import wiremind_kubernetes.kubernetes_helper


def test_kubernetes_client_additional_arguments_core_v1_api(mocker: MockerFixture) -> None:
    """
    Test that we add mandatory args to each function call of kubernetes client
    """
    mocked_read_namespaced_pod = mocker.patch("kubernetes.client.CoreV1Api.read_namespaced_pod")
    mocked_create_namespaced_pod = mocker.patch("kubernetes.client.CoreV1Api.create_namespaced_pod")

    kubernetes_helper = wiremind_kubernetes.kubernetes_helper.KubernetesHelper(
        dry_run=True, should_load_kubernetes_config=False
    )

    kubernetes_helper.client_corev1_api.read_namespaced_pod("foo", "bar")
    mocked_read_namespaced_pod.assert_called_once_with("foo", "bar", pretty=True)

    kubernetes_helper.client_corev1_api.create_namespaced_pod("foo", "bar")
    mocked_create_namespaced_pod.assert_called_once_with("foo", "bar", pretty=True, dry_run="All")
