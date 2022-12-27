import json
import logging
import subprocess
import sys
import urllib
from typing import Any, Dict

from wiremind_kubernetes import run_command

logger = logging.getLogger(__name__)


def check_not_using_wiremind_cluster() -> None:
    """
    Will sys.exit(1) if kubectl current context api server is not a test cluster (like kind, minikube, etc)
    """
    logger.info("[CLUSTER-CONFIG]: Making sure the tests are not running against the main cluster...")

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
        logger.error("Attempted to run tests with non-test cluster %s, abort!", api_server)
        sys.exit(1)


def get_k8s_username() -> str:
    """
    Return the Kind cluster's username.
    """
    command = """kubectl config view -o json | jq '. as $o
    | ."current-context" as $current_context_name
    | $o.contexts[] | select(.name == $current_context_name) as $context
    | $o.users[] | select(.name == $context.context.user) as $user
    | $user.name'"""
    # dex-k8s-authenticator sets the user to: user={{ .Username}}-{{.ClusterName }}`
    # https://github.com/mintel/dex-k8s-authenticator/blob/master/templates/linux-mac-common.html#L101
    username = (
        subprocess.check_output(command, shell=True, universal_newlines=True).replace('"', "").strip().split("-")[0]
    )
    assert username
    return username


def kubectl_get_json(*, resource: str, namespace: str, name: str) -> Dict[str, Any]:
    output, *_ = run_command(
        f"kubectl get {resource} {name} -n {namespace} --ignore-not-found -o json", return_result=True
    )
    return json.loads(output or "{}")
