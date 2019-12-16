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
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "kubernetes>=10.0.0",
    ],
    extras_require={
        'dev': [
            'coverage',
            'flake8',
            'flake8-mutable',
            'mock',
            'nose>=1.0',
            'pytest',
            # 1.13 (through https://github.com/pytest-dev/pytest-mock/commit/7bddcd53d287a59150d22e6496bcf20af44c3378)
            # broke our tests
            'pytest-mock==1.12.1',
            'pip-tools>=3.7.0',
            'pip-tools',
        ]
    },
    python_requires='>=3.5.0',
)
