# -*- coding: utf-8 -*-
import kubernetes


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
