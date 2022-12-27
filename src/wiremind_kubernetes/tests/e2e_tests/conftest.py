import logging
import os
import time
from typing import Generator

import kubernetes
import pytest
from pytest_mock import MockerFixture

import wiremind_kubernetes
from wiremind_kubernetes.tests.e2e_tests.helpers import check_not_using_wiremind_cluster
from wiremind_kubernetes.utils import run_command

E2E_CLUSTER_MANIFESTS = "tests/e2e_tests/manifests"
absolute_path = os.path.dirname(os.path.join(os.path.abspath(wiremind_kubernetes.__file__)))
TEST_NAMESPACE = "wiremind-kube-e2e-test"


logging.getLogger("wiremind_kubernetes").setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def k8s_client_request_function(mocker: MockerFixture) -> Generator:
    yield mocker.spy(kubernetes.client.api_client.ApiClient, "request")


@pytest.fixture(scope="session", autouse=True)
def setUpE2E() -> None:
    check_not_using_wiremind_cluster()


def delete_namespace() -> None:
    run_command(
        f"kubectl delete namespace {TEST_NAMESPACE} --wait --grace-period=1",
    )


@pytest.fixture
def populate_cluster() -> Generator[None, None, None]:
    run_command(
        f"kubectl apply -f {absolute_path}/../../CustomResourceDefinition-expecteddeploymentscales.yaml",
    )

    try:
        run_command(
            f"kubectl create namespace {TEST_NAMESPACE}",
        )
        run_command(
            f"kubectl apply -f {absolute_path}/{E2E_CLUSTER_MANIFESTS} --namespace {TEST_NAMESPACE} --wait",
        )

        concerned_dm = wiremind_kubernetes.KubernetesDeploymentManager(
            use_kubeconfig=True,
            namespace=TEST_NAMESPACE,
            release_name="concerned",
        )

        unconcerned_dm = wiremind_kubernetes.KubernetesDeploymentManager(
            use_kubeconfig=True,
            namespace=TEST_NAMESPACE,
            release_name="unconcerned",
        )

        ready = False
        for _ in range(1, 10):
            logger.info("Waiting for deployments to be started...")
            if not concerned_dm.is_deployment_ready("concerned") or not unconcerned_dm.is_deployment_ready(
                "unconcerned"
            ):
                logger.info("All Deployments not ready yet, waiting...")
                run_command(f"kubectl get pods --namespace {TEST_NAMESPACE}")
                time.sleep(5)
            else:
                ready = True
                break
        if not ready:
            run_command(
                f"kubectl delete namespace {TEST_NAMESPACE} --wait",
            )
            raise Exception("Could not start deployments.")
    except:  # noqa E722
        delete_namespace()
        raise

    yield

    delete_namespace()


@pytest.fixture
def create_namespace() -> Generator[None, None, None]:
    run_command(
        f"kubectl create namespace {TEST_NAMESPACE}",
    )

    run_command(
        f"kubectl apply -f {absolute_path}/{E2E_CLUSTER_MANIFESTS}/0_priorityclasses.yml"
        f" --namespace {TEST_NAMESPACE} --wait"
    )

    yield

    run_command(
        f"kubectl delete namespace {TEST_NAMESPACE} --wait",
    )


@pytest.fixture
def concerned_dm() -> wiremind_kubernetes.KubernetesDeploymentManager:
    return wiremind_kubernetes.KubernetesDeploymentManager(
        use_kubeconfig=True,
        namespace=TEST_NAMESPACE,
        release_name="concerned",
    )


@pytest.fixture
def unconcerned_dm() -> wiremind_kubernetes.KubernetesDeploymentManager:
    return wiremind_kubernetes.KubernetesDeploymentManager(
        use_kubeconfig=True,
        namespace=TEST_NAMESPACE,
        release_name="unconcerned",
    )
