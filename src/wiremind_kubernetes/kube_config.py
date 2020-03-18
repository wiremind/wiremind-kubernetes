# -*- coding: utf-8 -*-
import logging
import os

import kubernetes


logger = logging.getLogger(__name__)


def _get_kube_config_loader_for_yaml_file_with_persistence(
    filename, persist_config=False, **kwargs
):

    kcfg = kubernetes.config.kube_config.KubeConfigMerger(filename)
    if persist_config and "config_persister" not in kwargs:
        kwargs["config_persister"] = lambda unused_config_value: kcfg.save_changes()

    return kubernetes.config.kube_config.KubeConfigLoader(
        config_dict=kcfg.config, config_base_path=None, **kwargs
    )


def _load_kubeconfig():
    # persist tokens after refreshing them.
    kubernetes.config.kube_config._get_kube_config_loader_for_yaml_file = (
        _get_kube_config_loader_for_yaml_file_with_persistence  # noqa
    )
    kubernetes.config.load_kube_config()
    logger.debug("Kubernetes configuration successfully set.")


def _load_incluster_config():
    kubernetes.config.load_incluster_config()
    logger.debug("Kubernetes configuration successfully set.")


def load_kubernetes_config(use_kubeconfig=None):
    """
    Load kubernetes configuration in memory, either from incluster method or from kubeconfig.
    :param use_kubeconfig:
        If True: Use ~/.kube/config file to authenticate.
        If false: use kubernetes built-in incluster mechanism.
        If None, will try to load built-in incluster mechanism, then try config file.
        Defaults to None.
    """
    if use_kubeconfig is True:
        _load_kubeconfig()
    if use_kubeconfig is False:
        _load_incluster_config()
    if use_kubeconfig is None:
        if os.path.exists(kubernetes.config.incluster_config.SERVICE_TOKEN_FILENAME):
            _load_incluster_config()
        else:
            _load_kubeconfig()
