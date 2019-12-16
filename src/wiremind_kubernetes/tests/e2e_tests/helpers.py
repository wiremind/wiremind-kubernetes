import logging
import subprocess
import sys
import urllib

import kubernetes
import pytest
import unittest

from wiremind_kubernetes.utils import run_command

logger = logging.getLogger(__name__)


def check_not_using_wiremind_cluster():
    """
    Will sys.exit(1) if kubectl current context api server is not a test cluster (like kind, minikube, etc)
    """
    logger.info("[CLUSTER-CONFIG]: Make sure the tests are not running against the main cluster")

    api_server = subprocess.check_output(
        "kubectl config view --minify | grep server | cut -f 2- -d ':' | tr -d ' '",
        shell=True,
        universal_newlines=True,
    )
    whitelisted_api_server_hostname_list = [
        "localhost",  # minikube
        "127.0.0.1",  # kind
        "kubernetes.docker.internal",  # Docker for Mac
    ]
    hostname = urllib.parse.urlparse(api_server.lower().strip()).hostname
    if hostname not in whitelisted_api_server_hostname_list:
        logger.error(
            "Attempted to run tests with non-test cluster %s, abort!", api_server
        )
        sys.exit(1)


def get_k8s_username():
    """
    Return the Kind cluster's username.
    """
    command = "kubectl config view -o jsonpath='{.users[0].name}'"
    # dex-k8s-authenticator sets the user to: user={{ .Username}}-{{.ClusterName }}`
    # https://github.com/mintel/dex-k8s-authenticator/blob/master/templates/linux-mac-common.html#L101
    username = run_command(command, return_output=True)[0].strip().split('-')[0]
    assert username

    return username


def set_up_calico_networking_plugin_if_kind():
    current_context = subprocess.check_output("kubectl config current-context | tr -d ' '",
                                              shell=True, universal_newlines=True)
    if "kind" not in current_context:
        return

    subprocess.check_output("kubectl apply --overwrite=false "
                            "-f https://docs.projectcalico.org/v3.8/manifests/calico.yaml",
                            shell=True, universal_newlines=True)
    logger.info("[CLUSTER-CONFIG]: Calico has been set up")


@pytest.fixture(scope='function')
def k8s_client_request_function(mocker):
    yield mocker.spy(kubernetes.client.api_client.ApiClient, 'request')


@pytest.fixture(scope='session', autouse=True)
def setUpE2E():
    check_not_using_wiremind_cluster()
    set_up_calico_networking_plugin_if_kind()


class E2ETestUnittest(unittest.TestCase):  # For projects that still use unittest/nosetest
    @classmethod
    def setUpClass(cls):
        check_not_using_wiremind_cluster()
        set_up_calico_networking_plugin_if_kind()
