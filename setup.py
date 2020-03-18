"""
wiremind-kubernetes

Copyright 2018, wiremind.
"""
from setuptools import setup, find_packages

with open("VERSION") as version_file:
    version = version_file.read().strip()

extra_require_test = [
    "mock",
    "pytest",
    # 1.13 (through https://github.com/pytest-dev/pytest-mock/commit/7bddcd53d287a59150d22e6496bcf20af44c3378)
    # broke our tests
    "pytest-mock==1.12.1",
]
extra_require_mypy = [
    "mypy",
]
extra_require_dev = (
    ["flake8", "flake8-mutable", "pip-tools>=3.7.0",]
    + extra_require_mypy
    + extra_require_test
)


setup(
    name="wiremind-kubernetes",
    version=version,
    description="Helper for Kubernetes.",
    author="wiremind",
    author_email="dev@wiremind.fr",
    url="https://gitlab.cayzn.com/wiremind/common/wiremind-kubernetes.git",
    license="Proprietary",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=True,
    install_requires=["kubernetes>=10.0.0",],
    extras_require={
        "dev": extra_require_dev,
        "mypy": extra_require_mypy,
        "test": extra_require_test,
    },
    python_requires=">=3.6.0",
)
