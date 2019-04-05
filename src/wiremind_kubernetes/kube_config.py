# -*- coding: utf-8 -*-
import logging
import os

import kubernetes


logger = logging.getLogger(__name__)


# Fixes https://github.com/kubernetes-client/python-base/issues/65
def _load_oid_token(self, provider):
    import base64
    import datetime
    from kubernetes.config.dateutil import UTC
    import json
    from six import PY3
    if 'config' not in provider:
        return

    if 'name' not in provider or 'config' not in provider:
        return

    if provider['name'] != 'oidc':
        return

    parts = provider['config']['id-token'].split('.')

    if len(parts) != 3:  # Not a valid JWT
        return None

    padding = (4 - len(parts[1]) % 4) * '='

    if PY3:
        jwt_attributes = json.loads(
            base64.b64decode(parts[1] + padding).decode('utf-8')
        )
    else:
        jwt_attributes = json.loads(
            base64.b64decode(parts[1] + padding)
        )

    expire = jwt_attributes.get('exp')

    if ((expire is not None) and  # noqa
        (kubernetes.config.kube_config._is_expired(datetime.datetime.fromtimestamp(expire, tz=UTC)))):
        self._refresh_oidc(provider)

        if self._config_persister:
            self._config_persister(self._config.value)

    self.token = "Bearer %s" % provider['config']['id-token']

    return self.token


def _load_kubeconfig():
    # Fixes https://github.com/kubernetes-client/python-base/issues/65
    kubernetes.config.kube_config.KubeConfigLoader._load_oid_token = _load_oid_token  # noqa
    kubernetes.config.load_kube_config()
    logger.info('Kubernetes configuration successfully set.')


def _load_incluster_config():
    kubernetes.config.load_incluster_config()
    logger.info('Kubernetes configuration successfully set.')


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
