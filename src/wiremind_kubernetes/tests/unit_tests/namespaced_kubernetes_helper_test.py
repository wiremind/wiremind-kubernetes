from pytest_mock import MockerFixture
import pytest

import wiremind_kubernetes


@pytest.mark.parametrize(
    "phase, expected_stopped",
    [("Failed", True), ("Succeeded", True), ("Running", False)],
)
def test_is_deployment_stopped(mocker: MockerFixture, phase: str, expected_stopped: bool) -> None:
    """
    Test that we only consider non-terminal Pods as living Pods
    """
    mocker.patch("kubernetes.client.AppsV1Api")
    mocker.patch("kubernetes.client.CoreV1Api")
    mocker.patch("kubernetes.client.BatchV1Api")
    mocker.patch("kubernetes.client.CustomObjectsApi")

    class DummyStatusObject:
        def __init__(self) -> None:
            self.phase = phase

    class DummyPodObject:
        status = DummyStatusObject()

    namespaced_kubernetes_helper = wiremind_kubernetes.NamespacedKubernetesHelper(
        should_load_kubernetes_config=False, namespace="foo"
    )

    mocker.patch(
        "wiremind_kubernetes.NamespacedKubernetesHelper._get_pods_from_deployment",
        return_value=[DummyPodObject()],
    )

    assert namespaced_kubernetes_helper.is_deployment_stopped("bar") is expected_stopped
