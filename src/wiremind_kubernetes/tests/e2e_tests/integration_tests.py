import logging
import os
import subprocess
import time

import wiremind_kubernetes
from wiremind_kubernetes.tests.e2e_tests.helpers import (
    check_not_using_wiremind_cluster,
    E2ETestUnittest,
)

E2E_CLUSTER_MANIFESTS = "tests/e2e_tests/manifests"
logger = logging.getLogger(__name__)
absolute_path = os.path.dirname(
    os.path.join((os.path.abspath(wiremind_kubernetes.__file__)))
)


class StartStopTest(E2ETestUnittest):
    def setUp(self):
        check_not_using_wiremind_cluster()
        subprocess.check_output(
            "(for n in 1 2 3 4 5; do kubectl apply -f {}/{} &&"
            " break; sleep 1; done);".format(absolute_path, E2E_CLUSTER_MANIFESTS),
            shell=True,
            universal_newlines=True,
        )

        self.concerned_dm = wiremind_kubernetes.KubernetesDeploymentManager(
            use_kubeconfig=True,
            deployment_namespace="default",
            release_name="concerned",
        )
        self.unconcerned_dm = wiremind_kubernetes.KubernetesDeploymentManager(
            use_kubeconfig=True,
            deployment_namespace="default",
            release_name="unconcerned",
        )

        for _ in range(1, 10):
            logger.info("Waiting for deployments to be started...")
            if not (
                self.concerned_dm.is_deployment_stopped("concerned")
                and self.concerned_dm.is_deployment_stopped("concerned-new-style")
                and self.unconcerned_dm.is_deployment_stopped("unconcerned")
                and self.unconcerned_dm.is_deployment_stopped("unconcerned-new-style")
            ):
                break
            else:
                logger.info("All deployment not started yet, waiting...")
                time.sleep(5)
        else:
            self.assertFalse(self.concerned_dm.is_deployment_stopped("concerned"))
            self.assertFalse(
                self.concerned_dm.is_deployment_stopped("concerned-new-style")
            )
            self.assertFalse(self.unconcerned_dm.is_deployment_stopped("unconcerned"))
            self.assertFalse(
                self.unconcerned_dm.is_deployment_stopped("unconcerned-new-style")
            )

    def test_stop_all(self):
        """
        stop all deployments THAT HAVE AN EDS in the namespace default.
        """
        self.concerned_dm.stop_pods()
        self.assertTrue(self.concerned_dm.is_deployment_stopped("concerned"))
        self.assertTrue(self.concerned_dm.is_deployment_stopped("concerned-new-style"))
        self.assertFalse(self.unconcerned_dm.is_deployment_stopped("unconcerned"))
        self.assertFalse(
            self.unconcerned_dm.is_deployment_stopped("unconcerned-new-style")
        )
