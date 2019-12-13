import logging
import subprocess
import sys
import unittest
import urllib


logger = logging.getLogger(__name__)


def check_not_using_wiremind_cluster():
    """
    Will sys.exit(1) if kubectl current context api server is not a test cluster (like kind, minikube, etc)
    """
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
        logger.info(
            "Attempted to run tests with non-test cluster %s, abort!", api_server
        )
        sys.exit(1)


class E2ETestUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        check_not_using_wiremind_cluster()
