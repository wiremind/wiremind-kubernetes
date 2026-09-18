import kubernetes
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
        "wiremind_kubernetes.NamespacedKubernetesHelper._get_pods_from_deployment",
        return_value=[DummyPodObject()],
    )

    assert namespaced_kubernetes_helper.is_deployment_stopped("bar")


def test_scale_down_statefulset_does_not_raise_if_statefulset_missing(mocker: MockerFixture) -> None:
    """
    Regression test for #5: wiremind-kube (chartreuse, mayo) should not raise if a
    StatefulSet related to an ExpectedDeploymentScale does not exist, it should print
    a warning and continue. scale_down_deployment already handled this via
    @retry_kubernetes_request; its StatefulSet sibling, scale_down_statefulset, was
    missing the same decorator and would raise on a 404 instead.
    """
    mocker.patch("kubernetes.client.AppsV1Api")
    mocker.patch("kubernetes.client.CoreV1Api")
    mocker.patch("kubernetes.client.BatchV1Api")
    mocker.patch("kubernetes.client.CustomObjectsApi")

    namespaced_kubernetes_helper = wiremind_kubernetes.NamespacedKubernetesHelper(
        should_load_kubernetes_config=False, namespace="foo"
    )

    mocker.patch(
        "wiremind_kubernetes.NamespacedKubernetesHelper.get_statefulset_scale",
        side_effect=kubernetes.client.rest.ApiException(status=404),
    )
    patch_scale = mocker.patch.object(
        namespaced_kubernetes_helper.client_appsv1_api, "patch_namespaced_stateful_set_scale"
    )

    # Must not raise.
    namespaced_kubernetes_helper.scale_down_statefulset("missing-statefulset")

    patch_scale.assert_not_called()


def test_scale_up_statefulset_does_not_raise_if_statefulset_missing(mocker: MockerFixture) -> None:
    """
    Same regression as above (#5), for the scale-up path.
    """
    mocker.patch("kubernetes.client.AppsV1Api")
    mocker.patch("kubernetes.client.CoreV1Api")
    mocker.patch("kubernetes.client.BatchV1Api")
    mocker.patch("kubernetes.client.CustomObjectsApi")

    namespaced_kubernetes_helper = wiremind_kubernetes.NamespacedKubernetesHelper(
        should_load_kubernetes_config=False, namespace="foo"
    )

    mocker.patch(
        "wiremind_kubernetes.NamespacedKubernetesHelper.get_statefulset_scale",
        side_effect=kubernetes.client.rest.ApiException(status=404),
    )
    patch_scale = mocker.patch.object(
        namespaced_kubernetes_helper.client_appsv1_api, "patch_namespaced_stateful_set_scale"
    )

    # Must not raise.
    namespaced_kubernetes_helper.scale_up_statefulset("missing-statefulset")

    patch_scale.assert_not_called()
