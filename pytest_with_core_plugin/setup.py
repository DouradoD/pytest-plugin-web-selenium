# setup.py
from setuptools import setup, find_packages

setup(
    name="pytest_with_core_plugin",
    version="0.1.0",
    author="Diogo Dourado",
    author_email="diogo.augusto.dourado@gmail.com",
    description="Minimum required for write your first Automation test using Pytest and Selenium. "
                "Note: The core is the responsible for the setup and tear-down",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="LICENSE",
    python_requires=">=3.9",
    install_requires=[
        "core>=0.1.0",
    ],
    packages=find_packages(where="pytest_with_core_plugin"),
    package_dir={"": "pytest_with_core_plugin"},
)