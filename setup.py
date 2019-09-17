"""
wiremind-kubernetes

Copyright 2018, wiremind.
"""
from setuptools import setup, find_packages

with open('VERSION') as version_file:
    version = version_file.read().strip()


setup(
    name="wiremind-kubernetes",
    version=version,
    description="Helper for Kubernetes.",
    author="wiremind",
    author_email="dev@wiremind.fr",
    url="https://gitlab.cayzn.com/wiremind/common/wiremind-kubernetes.git",
    license="Proprietary",
    packages=find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "kubernetes>=10.0.0",
        "future"
    ],
    extras_require={
        'dev': [
            'coverage',
            'flake8',
            'flake8-mutable',
            'mock',
            'nose>=1.0',
            'pip-tools>=3.7.0',
            'pip-tools',
        ]
    },
)
