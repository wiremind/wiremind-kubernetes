# -*- coding: utf-8 -*-
from future.standard_library import install_aliases

install_aliases()

import functools
import logging
import shlex
import subprocess
import time

import kubernetes


logger = logging.getLogger(__name__)


def _run_command(command):
    """
    Run command, print stdout/stderr, check that command exited correctly, return stdout/err
    """
    logger.info("Running %s" % command)
    process = subprocess.Popen(
        shlex.split(command),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    out, err = process.communicate()
    if out:
        logger.info(out)
    if err:
        logger.error(err)
    if process.returncode:
        raise subprocess.CalledProcessError(process.returncode, command)
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
