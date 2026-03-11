"""
wiremind-kubernetes
"""

from setuptools import find_packages, setup

with open("VERSION") as version_file:
    version = version_file.read().strip()

extra_require_test = [
    "mock",
    "pytest",
    "pytest-mock",
]
extra_require_mypy = [
    "mypy",
]
extra_require_dev = (
    [
        "ruff",
        "safety",
    ]
    + extra_require_mypy
    + extra_require_test
)


setup(
    name="wiremind-kubernetes",
    version=version,
    description="Helper for Kubernetes.",
    long_description="""This Python library is a high-level set of Kubernetes Helpers allowing either
to manage individual standard Kubernetes controllers (Deployment, StatefulSets, etc) or a logical set
of standard Kubernetes controllers through the `expecteddeploymentscales.wiremind.io` CRD (for example
allowing to scale down ALL Deployments of a Helm Release marked as such).""",
    author="Wiremind",
    author_email="dev@wiremind.io",
    url="https://github.com/wiremind/wiremind-kubernetes",
    license="LGPLv3+",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"wiremind_kubernetes": ["py.typed"]},
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "kubernetes>=18.0.0",
    ],
    extras_require={
        "dev": extra_require_dev,
        "mypy": extra_require_mypy,
        "test": extra_require_test,
    },
    python_requires=">=3.13.0",
    keywords=["kubernetes"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
)
