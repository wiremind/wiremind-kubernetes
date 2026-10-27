import pytest
from pytest_mock import MockerFixture

# Every generated client class that KubernetesHelper wraps.
KUBERNETES_CLIENT_CLASSES = [
    "AdmissionregistrationV1Api",
    "AppsV1Api",
    "AutoscalingV2Api",
    "BatchV1Api",
    "CoreV1Api",
    "CustomObjectsApi",
    "NetworkingV1Api",
    "RbacAuthorizationV1Api",
    "StorageV1Api",
]


@pytest.fixture
def mocked_kubernetes_clients(mocker: MockerFixture) -> None:
    """
    Mock every generated client class, so that no test sends a request to an API server.
    """
    for client_class in KUBERNETES_CLIENT_CLASSES:
        mocker.patch(f"kubernetes.client.{client_class}")
