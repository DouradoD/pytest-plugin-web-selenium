from setuptools import setup, find_packages

setup(
    name="core",
    version="0.1.0",
    author="Diogo Dourado",
    author_email="diogo.augusto.dourado@gmail.com",
    description="Custom Core for Pytest.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pytest_core",
    license="MIT",
    packages=find_packages(where="."),
    python_requires=">=3.9",
    install_requires=[
        "selenium==4.29.0",
        "webdriver-manager==4.0.2",
        "pytest==8.3.4",
        "pytest-bdd==8.1.0",
        "pytest-html==4.1.1",
    ],
    entry_points={
        "pytest11": [
            "core = core.custom_pytest_setup",  # Entry point for pytest plugin
        ],
    },
)