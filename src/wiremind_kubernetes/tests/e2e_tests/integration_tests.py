import unittest
import wiremind_kubernetes


class StartStopTest(unittest.TestCase):
    def setUp(self):
        self.concerned_dm = wiremind_kubernetes.KubernetesDeploymentManager(
            use_kubeconfig=True, deployment_namespace="default", release_name="concerned"
        )
        self.unconcerned_dm = wiremind_kubernetes.KubernetesDeploymentManager(
            use_kubeconfig=True, deployment_namespace="default", release_name="unconcerned"
        )

    def test_stop_all(self):
        """
        stop all deployments THAT HAVE AN EDS in the namespace default.
        """
        print("-----")
        self.concerned_dm.stop_pods()
        self.assertTrue(self.concerned_dm.is_deployment_stopped("concerned"))
        self.assertTrue(self.unconcerned_dm.is_deployment_stopped("unconcerned"))
        print("-----")
