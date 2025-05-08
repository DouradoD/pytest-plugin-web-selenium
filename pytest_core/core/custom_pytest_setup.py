import pytest
from core.session_info import SessionInfo
from core.custom_driver import CustomerDriver
import logging

from .custom_logger import logger

def pytest_addoption(parser):

    parser.addoption("--session", action="store", default=None,
                     help="The session info to use during the test, it is a required field if you are not using the --capabilities_path")
    parser.addoption("--capabilities", action="store", default=False,
                     help="The session info to use during the test, it is a required field if you are not using the --capabilities_path")
    parser.addoption("--capabilities_path", action="store", default=None,
                     help="Specify the capabilities path, C:./../capabilities.json, by default is None")
    parser.addoption("--browserOptions", action="store", default=None,
                     help="The Selenium browseOption.")



@pytest.fixture(scope='session')
def driver(request):
    logger.info("Starting the driver: Building the Driver...")
    logger.info("Creating the driver...")
    session_info = SessionInfo(request_config=request.config).get_session_info
    driver = CustomerDriver(session_info=session_info)
    logger.info(driver._session_info)




    driver = driver.driver(timeout=15)
    driver.maximize_window()


    yield driver

    logger.info("Finishing the Driver/Tests...")
    driver.quit()


def pytest_report_teststatus(report):
    # Only modify the status for the "call" phase (test execution)
    if report.when == "call":
        if report.passed:
            return "✅ ", "PASS", "PASSED"
        elif report.failed:
            return "❌ ", "FAIL", "FAILED"
    # Return None for other phases to avoid modifying their status
    return None