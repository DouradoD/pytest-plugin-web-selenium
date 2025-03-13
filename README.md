## Simple Pytest Project with Selenium
A simple project to demonstrate how to split setup and teardown logic into different packages using pytest and Selenium.

Table of Contents
1. Project Structure 
2. Setup 
   3. Create and Activate Virtual Environment 
   4. Install Dependencies 
5. How to Run 
   6. Run Tests via Command Line 
   7. Run Tests via runner.py 
8. Logging Configuration (WIP)

## Setup
````
pytest-web-selenium/
├── pytest_core/                  # Core plugin with setup and teardown logic / Driver builder
│     ├── core/                   # Core functionality
│     │     └── __init__.py
│     ├── logging.ini             # Logging configuration  WIP/TBD
│     ├── LICENSE
│     ├── README.md
│     └── setup.py
├── pytest_zero/                  # Test module
│     ├── tests/                  # Test files
│     │     └── __init__.py
│     ├── LICENSE
│     ├── README.md
│     └── setup.py
````

## Setup

1. Create a virtual env:
````bash
   python -m venv .venv
````
2. Activate the venv:
Linux
````bash
   source .venv/bin/activate
````
Windows
````bash
   .venv\Scripts\activate
   or
   source .venv\Scripts\activate

````
## Install dependencies

1. Install the pytest_core:
````bash
    cd pytest_core
    pip install .
````
2. Install additional dependencies, if required:
````bash
    cd ../pytest_zero
    pip install .
````

## How to Run
### Run Tests via Command Line

1. Navigate to the pytest_zero directory:
````bash
    cd ../pytest_zero
    pip install .
````
2. Navigate to the pytest_zero directory:
````bash
    pytest -s -v --log-level=info --tb=auto --html=report.html --self-contained-html
````
- -s: Disable output capturing (show logs in the terminal).

- -v: Run in verbose mode.

- --log-level=info: Set the logging level to INFO.

- --tb=auto: Enable traceback for failed tests.

- --html=report.html: Generate an HTML report.

- --self-contained-html: Create a self-contained HTML report.

Note: Run the command below to check for more details:
````bash
    pytest --help
````

### Run Tests via runner.py
1. Navigate to the pytest_zero directory:
````bash
    cd pytest_zero
````
2Navigate to the pytest_zero directory:
````bash
    python runner.py
````
Note: Inside this file contain the other attributes passed through the command-line

### License
LICENSE

### Support
For questions, issues, or feature requests, please open an issue on the GitHub repository.

### Acknowledgments
- Selenium: For browser automation. 
- pytest: For the testing framework. 
- pytest-bdd: For Behavior-Driven Development support. 
- pytest-html: For HTML reporting.

### Changelog
v0.1.0 (Initial Release)
- Added driver fixture for WebDriver management. 
- Integrated with pytest-bdd and pytest-html.