from typing import Optional


class WiremindKubernetesException(Exception):
    """
    Base wiremind-kubernetes Exception.
    """

    def __init__(self, message: Optional[str] = None):
        super().__init__()
        if message:
            self.message = message


class ExecError(WiremindKubernetesException):
    """
    An error occured while executing kubernetes command.
    """

    def __init__(self) -> None:
        super().__init__(message="An error occured while executing kubernetes command.")


class PodNotFound(WiremindKubernetesException):
    """
    A required pod was not found.
    """

    pass
