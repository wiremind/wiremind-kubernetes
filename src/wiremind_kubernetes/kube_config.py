import logging
import os
from typing import Optional

import kubernetes

logger = logging.getLogger(__name__)


def _load_kubeconfig(config_file: Optional[str] = None, context: Optional[str] = None) -> None:
    kubernetes.config.load_kube_config(config_file=config_file, context=context)
    logger.debug("Kubernetes configuration successfully set.")


def _load_incluster_config() -> None:
    kubernetes.config.load_incluster_config()
    logger.debug("Kubernetes configuration successfully set.")


def load_kubernetes_config(
    use_kubeconfig: Optional[bool] = None, config_file: Optional[str] = None, context: Optional[str] = None
) -> None:
    """
    Load kubernetes configuration in memory, either from incluster method or from kubeconfig.
    :param use_kubeconfig:
        If True: Use ~/.kube/config file to authenticate.
        If false: use kubernetes built-in incluster mechanism.
        If None, will try to load built-in incluster mechanism, then try config file.
        Defaults to None.
    :param config_file
        Name of the kube-config file.
    :param context
        Set the active context. If is set to None, current_context
        from config file will be used.
    """
    if os.environ.get("CLASSIC_K8S_CONFIG"):
        # We are in a Kind cluster for E2E test! Never use in cluster config.
        _load_kubeconfig(config_file=config_file, context=context)
        return

    if use_kubeconfig is True:
        _load_kubeconfig(config_file=config_file, context=context)
    elif use_kubeconfig is False:
        _load_incluster_config()
    elif use_kubeconfig is None:
        if os.path.exists(kubernetes.config.incluster_config.SERVICE_TOKEN_FILENAME):
            _load_incluster_config()
        else:
            _load_kubeconfig(config_file=config_file, context=context)
    else:
        logger.debug("Kubernetes configuration was not loaded!")
