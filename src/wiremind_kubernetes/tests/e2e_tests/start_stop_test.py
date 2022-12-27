import logging
import time

from pytest_mock import MockerFixture

import wiremind_kubernetes
from wiremind_kubernetes import KubernetesDeploymentManager
from wiremind_kubernetes.kubernetes_helper import HPA_ID_PREFIX
from wiremind_kubernetes.tests.e2e_tests.conftest import TEST_NAMESPACE
from wiremind_kubernetes.tests.e2e_tests.helpers import kubectl_get_json

logger = logging.getLogger(__name__)


# Side effect, but we don't really care
KubernetesDeploymentManager.SCALE_DOWN_MAX_WAIT_TIME = 30


def assert_hpa_scale_target_ref_name(*, hpa_name: str, scale_target_ref_name: str) -> None:
    assert (
        kubectl_get_json(resource="hpa", namespace=TEST_NAMESPACE, name=hpa_name)["spec"]["scaleTargetRef"]["name"]
        == scale_target_ref_name
    )


def are_deployments_ready(
    concerned_dm: KubernetesDeploymentManager, unconcerned_dm: KubernetesDeploymentManager
) -> bool:
    return (
        concerned_dm.is_deployment_ready("concerned")
        and concerned_dm.is_deployment_ready("concerned-very-high-priority")
        and concerned_dm.is_deployment_ready("concerned-high-priority")
        and unconcerned_dm.is_deployment_ready("unconcerned")
    )


def wait_for_deployments_ready(
    concerned_dm: KubernetesDeploymentManager, unconcerned_dm: KubernetesDeploymentManager
) -> None:
    for _ in range(1, 10):
        logger.info("Waiting for deployments to be started...")
        if not are_deployments_ready(concerned_dm, unconcerned_dm):
            logger.info("All Deployments not ready yet, waiting...")
            time.sleep(5)
        else:
            # OK!
            break
    else:
        assert are_deployments_ready(concerned_dm, unconcerned_dm)  # Last chance


def test_stop_start_all(
    concerned_dm: KubernetesDeploymentManager,
    unconcerned_dm: KubernetesDeploymentManager,
    populate_cluster: MockerFixture,
    mocker: MockerFixture,
) -> None:
    """
    Test that we stop/start all deployments that have an EDS in the namespace default
    and only them.
    """
    spied_scale_down_deployment = mocker.spy(wiremind_kubernetes.NamespacedKubernetesHelper, "scale_down_deployment")
    spied_are_deployments_stopped = mocker.spy(
        wiremind_kubernetes.KubernetesDeploymentManager, "_are_deployments_stopped"
    )

    concerned_dm.stop_pods()
    assert concerned_dm.is_deployment_stopped("concerned")
    assert concerned_dm.is_deployment_stopped("concerned-2")
    assert concerned_dm.is_deployment_stopped("concerned-very-high-priority")
    assert concerned_dm.is_deployment_stopped("concerned-high-priority")
    assert not unconcerned_dm.is_deployment_stopped("unconcerned")

    # concerned HPA were disabled
    assert_hpa_scale_target_ref_name(hpa_name="concerned", scale_target_ref_name=f"{HPA_ID_PREFIX}-concerned")
    assert_hpa_scale_target_ref_name(hpa_name="unconcerned", scale_target_ref_name="unconcerned")

    # Test stop order to see if we honor priority (for in-depth testing of priority, see unit tests)
    scale_down_call_list = spied_scale_down_deployment.call_args_list
    assert scale_down_call_list[0][0][1] == "concerned-very-high-priority"
    assert scale_down_call_list[-1][0][1] == "concerned-low-priority"
    mocked_wait_call_list = spied_are_deployments_stopped.call_args_list
    assert mocked_wait_call_list[0][0][1] == {"concerned-very-high-priority": 1}
    assert mocked_wait_call_list[-1][0][1] == {"concerned-low-priority": 1}

    concerned_dm.start_pods()

    wait_for_deployments_ready(concerned_dm, unconcerned_dm)

    assert not concerned_dm.is_deployment_stopped("concerned")
    assert not concerned_dm.is_deployment_stopped("concerned-2")
    assert not concerned_dm.is_deployment_stopped("concerned-high-priority")
    assert not concerned_dm.is_deployment_stopped("concerned-very-high-priority")
    assert not unconcerned_dm.is_deployment_stopped("unconcerned")

    # concerned HPA were re-enabled
    assert_hpa_scale_target_ref_name(hpa_name="concerned", scale_target_ref_name="concerned")
    assert_hpa_scale_target_ref_name(hpa_name="unconcerned", scale_target_ref_name="unconcerned")
