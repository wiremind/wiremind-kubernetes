import unittest

import wiremind_kubernetes


def test_stop_pods_priority(mocker):
    """
    Test that we honor priorities when stopping workloads.

    i.e that we stop all deployments with the highest priority first, then wait for all of those to be stopped
    then continue.
    """
    mocker.patch("kubernetes.client.AppsV1Api")
    mocker.patch("kubernetes.client.CoreV1Api")
    mocker.patch("kubernetes.client.BatchV1Api")
    mocker.patch("kubernetes.client.CustomObjectsApi")

    mocker.patch(
        "wiremind_kubernetes.KubernetesDeploymentManager._get_expected_deployment_scale_dict",
        return_value={
            0: {"last": 42},
            2: {
                "first": 17,
            },
            1: {
                "second": 17,
            },
        },
    )

    mocked_stop_deployments = mocker.patch("wiremind_kubernetes.KubernetesDeploymentManager._stop_deployments")
    mocked_wait_for_deployments_stopped = mocker.patch(
        "wiremind_kubernetes.KubernetesDeploymentManager._wait_for_deployments_stopped"
    )
    merged_mock = unittest.mock.Mock()
    merged_mock.attach_mock(mocked_stop_deployments, "_stop_deployments")
    merged_mock.attach_mock(mocked_wait_for_deployments_stopped, "_wait_for_deployments_stopped")

    kdm = wiremind_kubernetes.KubernetesDeploymentManager(
        should_load_kubernetes_config=False, namespace="foo", release_name="concerned", dry_run=True
    )
    kdm.stop_pods()

    expected_calls = [
        unittest.mock.call._stop_deployments({"first": 17}),
        unittest.mock.call._wait_for_deployments_stopped({"first": 17}),
        unittest.mock.call._stop_deployments({"second": 17}),
        unittest.mock.call._wait_for_deployments_stopped({"second": 17}),
        unittest.mock.call._stop_deployments({"last": 42}),
        unittest.mock.call._wait_for_deployments_stopped({"last": 42}),
    ]

    assert merged_mock.mock_calls == expected_calls
