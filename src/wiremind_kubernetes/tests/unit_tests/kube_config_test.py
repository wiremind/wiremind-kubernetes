import os
from typing import Dict, Generator, Optional

import kubernetes
import pytest
from pytest_mock import MockerFixture

import wiremind_kubernetes
from wiremind_kubernetes.kube_config import load_kubernetes_config


@pytest.fixture(scope="module", autouse=True)
def clean_os_environ() -> Generator:
    """
    Get rid of the env var "CLASSIC_K8S_CONFIG", this will be set if needed using tests parameterization
    """
    old_os_environ = os.environ.copy()
    os.environ.pop("CLASSIC_K8S_CONFIG", None)
    yield
    os.environ.clear()
    os.environ.update(old_os_environ)


@pytest.mark.parametrize(
    "use_kubeconfig, config_file, context, extra_env_vars, service_token_present, should_call",
    [
        (
            True,
            None,
            "context-1",
            {},
            False,
            "wiremind_kubernetes.kube_config.kubernetes.config.load_kube_config",
        ),
        (
            False,
            "/test/config",
            None,
            {},
            True,
            "wiremind_kubernetes.kube_config.kubernetes.config.load_incluster_config",
        ),
        (
            None,
            None,
            None,
            {},
            False,
            "wiremind_kubernetes.kube_config.kubernetes.config.load_incluster_config",
        ),
        (
            None,
            "/test/config",
            "context-2",
            {},
            True,
            "wiremind_kubernetes.kube_config.kubernetes.config.load_incluster_config",
        ),
        (
            True,
            None,
            None,
            {"CLASSIC_K8S_CONFIG": "1"},
            True,
            "wiremind_kubernetes.kube_config.kubernetes.config.load_kube_config",
        ),
        (
            False,
            "context-1",
            "/test/config",
            {"CLASSIC_K8S_CONFIG": "1"},
            True,
            "wiremind_kubernetes.kube_config.kubernetes.config.load_kube_config",
        ),
        (
            None,
            None,
            None,
            {"CLASSIC_K8S_CONFIG": "1"},
            True,
            "wiremind_kubernetes.kube_config.kubernetes.config.load_kube_config",
        ),
        (
            "anything",
            None,
            None,
            {"CLASSIC_K8S_CONFIG": "1"},
            True,
            "wiremind_kubernetes.kube_config.kubernetes.config.load_kube_config",
        ),
        (
            "",
            None,
            "context-1",
            {},
            True,
            None,
        ),
        (
            "something",
            "/test/config",
            "context-1",
            {},
            False,
            None,
        ),
    ],
)
def test_load_kubernetes_config_1(
    use_kubeconfig: Optional[bool],
    config_file: Optional[str],
    context: Optional[str],
    extra_env_vars: Dict[str, str],
    service_token_present: bool,
    should_call: Optional[str],
    mocker: MockerFixture,
) -> None:
    """
    Test that load_kubernetes_config calls the right kube loading function, when needed, with the right parameters.
    Only relevant cases are tested.
    """
    load_kube_config: str = "wiremind_kubernetes.kube_config.kubernetes.config.load_kube_config"
    load_incluster_config: str = "wiremind_kubernetes.kube_config.kubernetes.config.load_incluster_config"

    mocker.patch(load_kube_config)
    mocker.patch(load_incluster_config)
    # merge extra_env_vars with os.environ
    mocker.patch.dict(os.environ, extra_env_vars)
    # os.path.exists is used ONLY to check for token file in wiremind_kubernetes.kube_config for now
    mocker.patch("wiremind_kubernetes.kube_config.os.path.exists", kawrgs={"side_effect": service_token_present})

    load_kubernetes_config(use_kubeconfig=use_kubeconfig, config_file=config_file, context=context)

    if should_call == load_kube_config:
        kubernetes.config.load_kube_config.assert_called_once_with(config_file=config_file, context=context)
        assert wiremind_kubernetes.kube_config.kubernetes.config.load_incluster_config.call_count == 0
    elif should_call == load_incluster_config:
        kubernetes.config.load_incluster_config.assert_called_once_with()
        assert wiremind_kubernetes.kube_config.kubernetes.config.load_kube_config.call_count == 0
    else:
        assert wiremind_kubernetes.kube_config.kubernetes.config.load_kube_config.call_count == 0
        assert wiremind_kubernetes.kube_config.kubernetes.config.load_incluster_config.call_count == 0
