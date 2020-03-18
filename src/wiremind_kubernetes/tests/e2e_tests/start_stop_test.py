import logging
import time

logger = logging.getLogger(__name__)


def test_stop_start_all(concerned_dm, unconcerned_dm, populate_cluster):
    """
    stop all deployments THAT HAVE AN EDS in the namespace default.
    """
    concerned_dm.stop_pods()
    assert concerned_dm.is_deployment_stopped("concerned")
    assert concerned_dm.is_deployment_stopped("concerned-new-style")
    assert not unconcerned_dm.is_deployment_stopped("unconcerned")
    assert not unconcerned_dm.is_deployment_stopped("unconcerned-new-style")

    concerned_dm.start_pods()

    def are_deployments_ready():
        return (
            concerned_dm.is_deployment_ready("concerned")
            and concerned_dm.is_deployment_ready("concerned-new-style")
            and unconcerned_dm.is_deployment_ready("unconcerned")
            and unconcerned_dm.is_deployment_ready("unconcerned-new-style")
        )

    # XXX factor this
    for _ in range(1, 10):
        logger.info("Waiting for deployments to be started...")
        if not are_deployments_ready():
            logger.info("All Deployments not ready yet, waiting...")
            time.sleep(5)
        else:
            # OK!
            break
    else:
        assert are_deployments_ready()  # Last chance

    assert not concerned_dm.is_deployment_stopped("concerned")
    assert not concerned_dm.is_deployment_stopped("concerned-new-style")
    assert not unconcerned_dm.is_deployment_stopped("unconcerned")
    assert not unconcerned_dm.is_deployment_stopped("unconcerned-new-style")
