import kubernetes.client.rest
import pytest

from wiremind_kubernetes.utils import retry_kubernetes_request, retry_kubernetes_request_no_ignore


def test_no_retry_required() -> None:
    counter = 0

    @retry_kubernetes_request
    def succeeds() -> str:
        nonlocal counter
        counter += 1
        return "success"

    r = succeeds()

    assert r == "success"
    assert counter == 1


def test_retries_once() -> None:
    counter = 0

    @retry_kubernetes_request
    def fails_once() -> str:
        nonlocal counter
        counter += 1
        if counter < 2:
            raise kubernetes.client.rest.ApiException("failed")
        else:
            return "success"

    r = fails_once()
    assert r == "success"
    assert counter == 2


def test_limit_is_reached() -> None:
    counter = 0

    @retry_kubernetes_request
    def always_fails() -> None:
        nonlocal counter
        counter += 1
        raise kubernetes.client.rest.ApiException("failed")

    with pytest.raises(kubernetes.client.rest.ApiException):
        always_fails()
    assert counter == 2


def test_404_correctly_handled() -> None:
    counter = 0

    @retry_kubernetes_request
    def notfound() -> None:
        nonlocal counter
        counter += 1
        raise kubernetes.client.rest.ApiException(status=404)

    r = notfound()

    assert r is None
    assert counter == 1


def test_404_correctly_ignored() -> None:
    """
    test that retry_kubernetes_request_no_ignore raises if 404 and does not retry
    """
    counter = 0

    @retry_kubernetes_request_no_ignore
    def notfound() -> None:
        nonlocal counter
        counter += 1
        raise kubernetes.client.rest.ApiException(status=404)

    with pytest.raises(kubernetes.client.rest.ApiException):
        r = notfound()
        assert r is None
    assert counter == 1
