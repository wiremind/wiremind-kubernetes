from pytest_mock import MockerFixture

import wiremind_kubernetes


def test_is_deployment_stopped_ignores_failed(mocker: MockerFixture) -> None:
    """
    Test that we don't consider failed (like evicted) Pods as living Pods
    """
    mocker.patch("kubernetes.client.AppsV1Api")
    mocker.patch("kubernetes.client.CoreV1Api")
    mocker.patch("kubernetes.client.BatchV1Api")
    mocker.patch("kubernetes.client.CustomObjectsApi")

    class DummyStatusObject:
        phase = "Failed"

    class DummyPodObject:
        status = DummyStatusObject()

    namespaced_kubernetes_helper = wiremind_kubernetes.NamespacedKubernetesHelper(
        should_load_kubernetes_config=False, namespace="foo"
    )

    mocker.patch(
        "wiremind_kubernetes.NamespacedKubernetesHelper._get_pods_from_deployment", return_value=[DummyPodObject()]
    )

    assert namespaced_kubernetes_helper.is_deployment_stopped("bar")
