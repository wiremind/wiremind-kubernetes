import json
import logging
import subprocess
import sys
import urllib
from typing import Any, Dict, List

import kubernetes

from wiremind_kubernetes import run_command

logger = logging.getLogger(__name__)

DEFAULT_TEST_IPS_WHITELISTED = [
    "localhost",  # minikube
    "127.0.0.1",  # kind
    "kubernetes.docker.internal",  # Docker for Mac
]

DEFAULT_TEST_NODES_WHITELISTED = ["minikube", "kind-control-plane", "kind", "kind-worker"]


def get_default_kube_context() -> str:
    """
    Retrieves the default kube context
    """
    try:
        return kubernetes.config.list_kube_config_contexts()[1]["name"]
    except kubernetes.config.config_exception.ConfigException:
        # Inside a Container maybe. This will make it use the incluster config.
        return ""


def is_ip_whitelisted(*, ips_whitelisted: List[str]) -> bool:
    api_server = subprocess.check_output(
        "kubectl config view --minify | grep server | cut -f 2- -d ':' | tr -d ' '",
        shell=True,
        text=True,
    )

    hostname = urllib.parse.urlparse(api_server.lower().strip()).hostname
    return hostname in ips_whitelisted


def is_node_whitelisted(*, nodes_whitelisted: List[str]) -> bool:
    output, *_ = run_command("kubectl get nodes -o name", return_result=True)
    cluster_nodes = [x for x in output.replace("node/", "").split("\n") if x != ""]
    for node in cluster_nodes:
        if node not in nodes_whitelisted:
            return False
    return True


def check_using_test_cluster(
    *,
    ips_whitelisted: List[str] = DEFAULT_TEST_IPS_WHITELISTED,
    nodes_whitelisted: List[str] = DEFAULT_TEST_NODES_WHITELISTED,
) -> bool:
    """
    Will sys.exit(1) if kubectl current context api server is not a test cluster (like kind, minikube, etc)
    """
    logger.info("[CLUSTER-CONFIG]: Making sure the tests are running against a test cluster...")

    kube_context = get_default_kube_context()

    if not is_ip_whitelisted(ips_whitelisted=ips_whitelisted) and not is_node_whitelisted(
        nodes_whitelisted=nodes_whitelisted
    ):
        logger.error(f"Attempted to run tests with non-test cluster <{kube_context}>, aborting!")
        sys.exit(1)
    return True


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
    username = subprocess.check_output(command, shell=True, text=True).replace('"', "").strip().split("-")[0]
    assert username
    return username


def kubectl_get_json(*, resource: str, namespace: str, name: str) -> Dict[str, Any]:
    output, *_ = run_command(
        f"kubectl get {resource} {name} -n {namespace} --ignore-not-found -o json", return_result=True
    )
    return json.loads(output or "{}")
