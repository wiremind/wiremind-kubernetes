# -*- coding: utf-8 -*-
from future.standard_library import install_aliases

install_aliases()

import functools
import logging
import shlex
import subprocess
import time

import kubernetes

from wiremind_kubernetes.exceptions import ExecError


logger = logging.getLogger(__name__)


def run_command(command, return_output=False, *args, **kw_args):
    """
    Run command, print stdout/stderr, check that command exited correctly, return stdout/err
    """
    logger.info("Running %s", command)
    if isinstance(command, str):
        command = shlex.split(command)
    process = subprocess.Popen(
        command,
        *args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        **kw_args
    )
    if return_output:
        out, err = process.communicate()
    else:
        for line in iter(process.stdout.readline, ''):
            logger.info(line.strip())
        process.wait()
    if process.returncode:
        raise subprocess.CalledProcessError(process.returncode, command)
    if return_output:
        return (out, err)


def retry_kubernetes_request(function):
    """
    Decorator that retries a failed Kubernetes API request if needed
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
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


def kubernetes_exec(commands, api, pod_name, namespace_name, container_name=None):
    logger.info('Connecting to "%s" pod from "%s" namespace', pod_name, namespace_name)
    resp = kubernetes.stream.stream(
        api.connect_get_namespaced_pod_exec, pod_name, namespace_name,
        command=['/bin/sh'],
        container=container_name,
        stderr=True, stdin=True, stdout=True, tty=False,
        _preload_content=False
    )

    while resp.is_open():
        resp.update(timeout=1)
        if resp.peek_stdout():
            logger.info(resp.read_stdout())
        if resp.peek_stderr():
            error_message = resp.read_stderr()
            logger.error(error_message)
            if 'FATAL' in error_message or 'ERROR' in error_message:
                raise ExecError()
        if commands:
            c = commands.pop(0)
            logger.info("Running command: %s\n", c)
            resp.write_stdin(c + "\n")
        else:
            break
