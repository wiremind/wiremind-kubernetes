import unittest

from pytest_mock import MockerFixture

import wiremind_kubernetes


def test_stop_pods_priority(mocker: MockerFixture) -> None:
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

    kdm = wiremind_kubernetes.KubernetesDeploymentManager(
        should_load_kubernetes_config=False, namespace="foo", release_name="concerned", dry_run=True
    )
    kdm.stop_pods()

    expected_calls = [
        unittest.mock.call._stop_deployments({"first": 17}),
        unittest.mock.call._stop_deployments({"second": 17}),
        unittest.mock.call._stop_deployments({"last": 42}),
    ]

    assert mocked_stop_deployments.mock_calls == expected_calls


def test_stop_deployments_correctly_wait(mocker: MockerFixture) -> None:
    """
    Test that we wait for deployments to be stopped
    """
    mocker.patch("kubernetes.client.AppsV1Api")
    mocker.patch("kubernetes.client.CoreV1Api")
    mocker.patch("kubernetes.client.BatchV1Api")
    mocker.patch("kubernetes.client.CustomObjectsApi")

    deployment_dict = {"my-pod": 42, "my-other-pod": 113}

    mocked_are_deployments_stopped = mocker.patch(
        "wiremind_kubernetes.KubernetesDeploymentManager._are_deployments_stopped", side_effect=[False, False, True]
    )

    kdm = wiremind_kubernetes.KubernetesDeploymentManager(
        should_load_kubernetes_config=False, namespace="foo", release_name="concerned", dry_run=True
    )
    kdm._stop_deployments(deployment_dict)

    expected_calls = [
        unittest.mock.call._are_deployments_stopped(deployment_dict),
        unittest.mock.call._are_deployments_stopped(deployment_dict),
        unittest.mock.call._are_deployments_stopped(deployment_dict),
    ]

    assert mocked_are_deployments_stopped.mock_calls == expected_calls
