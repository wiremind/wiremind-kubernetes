# -*- coding: utf-8 -*-
from future.standard_library import install_aliases

install_aliases()

import functools
import shlex
import subprocess
import time

import kubernetes


def _run_command(command):
    """
    Run command, print stdout/stderr, check that command exited correctly, return stdout/err
    """
    print("Running %s" % command)
    process = subprocess.Popen(
        shlex.split(command),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    out, err = process.communicate()
    if out:
        print(out)
    if err:
        print(err)
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
                print("Not found, ignoring.")
                return
            print(e)
            print("Retrying in 5 seconds...")
            time.sleep(5)
            return function(*args, **kwargs)
        finally:
            print("Done.")

    return wrapper
