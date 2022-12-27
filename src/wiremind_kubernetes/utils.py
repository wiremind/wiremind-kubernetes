import functools
import logging
import shlex
import subprocess
import time
from typing import Any, Callable, List, Optional, Tuple, Union

import kubernetes

from wiremind_kubernetes.exceptions import ExecError

logger = logging.getLogger(__name__)


def run_command(
    command: Union[List, str], return_result: bool = False, line_callback: Union[Callable, None] = None, **kw_args: Any
) -> Tuple[str, str, int]:
    """
    Run command, print stdout/stderr, check that command exited correctly, return stdout/err
    """
    logger.info("Running %s", command)
    if line_callback and return_result:
        raise ValueError("line_callback and return_result parameters are mutually incompatible.")

    if not line_callback:
        line_callback = logger.info

    interpreted_command: List[str]
    if isinstance(command, str):
        interpreted_command = shlex.split(command)
    else:
        interpreted_command = command

    process = subprocess.Popen(
        interpreted_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, **kw_args
    )

    if return_result:
        out, err = process.communicate()
        return (out, err, process.returncode)

    if process.stdout:
        for line in iter(process.stdout.readline, ""):
            line_callback(line.strip())
    process.wait()

    if process.returncode:
        raise subprocess.CalledProcessError(process.returncode, command)

    return "", "", 0


def retry_kubernetes_request(function: Callable) -> Callable:
    """
    Decorator that retries a failed Kubernetes API request if needed and ignores 404
    """

    @functools.wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return function(*args, **kwargs)
        except kubernetes.client.rest.ApiException as e:
            if e.status == 404:
                logger.warning("Not found, ignoring.")
                return
            logger.error(e)
            logger.info("Retrying in 5 seconds...")
            time.sleep(5)
            return function(*args, **kwargs)
        finally:
            logger.debug("Done.")

    return wrapper


def retry_kubernetes_request_no_ignore(function: Callable) -> Callable:
    """
    Decorator that retries a failed Kubernetes API request if needed and do NOT ignore 404 (raise if 404)
    """

    @functools.wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return function(*args, **kwargs)
        except kubernetes.client.rest.ApiException as e:
            if e.status == 404:
                raise
            logger.error(e)
            logger.info("Retrying in 5 seconds...")
            time.sleep(5)
            return function(*args, **kwargs)
        finally:
            logger.debug("Done.")

    return wrapper


def kubernetes_exec(
    commands: List[str], api: Any, pod_name: str, namespace_name: str, container_name: Optional[str] = None
) -> None:
    logger.info('Connecting to "%s" pod from "%s" namespace', pod_name, namespace_name)
    resp = kubernetes.stream.stream(
        api.connect_get_namespaced_pod_exec,
        pod_name,
        namespace_name,
        command=["/bin/sh"],
        container=container_name,
        stderr=True,
        stdin=True,
        stdout=True,
        tty=False,
        _preload_content=False,
    )

    while resp.is_open():
        resp.update(timeout=1)
        if resp.peek_stdout():
            logger.info(resp.read_stdout())
        if resp.peek_stderr():
            error_message = resp.read_stderr()
            logger.error(error_message)
            if "FATAL" in error_message or "ERROR" in error_message:
                raise ExecError()
        if commands:
            c = commands.pop(0)
            logger.info("Running command: %s\n", c)
            resp.write_stdin(c + "\n")
        else:
            break
