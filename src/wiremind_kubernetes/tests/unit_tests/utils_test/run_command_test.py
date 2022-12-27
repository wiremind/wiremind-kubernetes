import subprocess

import pytest
from pytest_mock import MockerFixture

from wiremind_kubernetes.utils import logger, run_command


def test_run_command_succeeded(mocker: MockerFixture) -> None:
    """
    Test that running a working command works as expected.
    """
    popen_spy = mocker.spy(subprocess, "Popen")
    log_spy = mocker.spy(logger, "info")

    run_command("echo lol")

    popen_spy.assert_called_once_with(
        ["echo", "lol"],
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    log_spy.assert_called_with("lol")


def test_run_command_with_array_succeeded(mocker: MockerFixture) -> None:
    """
    Test that running a working command given through array works as expected.
    """
    popen_spy = mocker.spy(subprocess, "Popen")
    log_spy = mocker.spy(logger, "info")

    run_command(["echo", "lol"])

    popen_spy.assert_called_once_with(
        ["echo", "lol"],
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    log_spy.assert_called_with("lol")


def test_run_command_succeeded_return_result(mocker: MockerFixture) -> None:
    """
    Test that running a working command using return_result=True works as expected.
    """
    popen_spy = mocker.spy(subprocess, "Popen")

    stdout, stderr, returncode = run_command("echo lol", return_result=True)

    popen_spy.assert_called_once_with(
        ["echo", "lol"],
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )

    assert stdout == "lol\n"
    assert stderr is None
    assert returncode == 0


def test_run_command_succeeded_line_callback(mocker: MockerFixture) -> None:
    """
    Test that running a working command using a custom line_callback works as expected.
    """
    result = []

    def line_callback(line: str) -> None:
        nonlocal result
        result.append(line)

    popen_spy = mocker.spy(subprocess, "Popen")

    run_command("echo lol", line_callback=line_callback)

    popen_spy.assert_called_once_with(
        ["echo", "lol"],
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )

    assert result == ["lol"]


def test_run_command_failed(mocker: MockerFixture) -> None:
    """
    Test that running a failing command works as expected.
    """
    popen_spy = mocker.spy(subprocess, "Popen")
    with pytest.raises(subprocess.CalledProcessError):
        run_command("false")
    popen_spy.assert_called_once_with(
        ["false"],
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )


def test_run_command_failed_still_show_output(mocker: MockerFixture) -> None:
    """
    Test that running a failing command still returns its output.
    """
    log_spy = mocker.spy(logger, "info")

    with pytest.raises(subprocess.CalledProcessError):
        run_command(["sh", "-c", "echo lol; false"])

    log_spy.assert_called_with("lol")


def test_run_command_failed_return_result(mocker: MockerFixture) -> None:
    """
    Test that running a failing command using return_result=True works as expected.
    """
    stdout, stderr, returncode = run_command(["sh", "-c", "echo lol; false"], return_result=True)

    assert stdout == "lol\n"
    assert stderr is None
    assert returncode == 1


def test_run_command_failed_line_callback(mocker: MockerFixture) -> None:
    """
    Test that running a failing command using custom line_callback works as expected.
    """
    result = []

    def line_callback(line: str) -> None:
        nonlocal result
        result.append(line)

    with pytest.raises(subprocess.CalledProcessError):
        run_command(["sh", "-c", "echo lol; false"], line_callback=line_callback)

    assert result == ["lol"]


def test_run_command_honors_args(mocker: MockerFixture) -> None:
    """
    Test that run_command honors kwargs.
    """
    popen_spy = mocker.spy(subprocess, "Popen")
    log_spy = mocker.spy(logger, "info")

    run_command(["echo lol; true"], shell=True)

    popen_spy.assert_called_once_with(
        ["echo lol; true"],
        shell=True,
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )

    log_spy.assert_called_with("lol")
