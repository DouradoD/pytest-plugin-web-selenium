import pytest
from core.session_info import SessionInfo
from core.custom_driver import CustomerDriver
import logging

from .custom_logger import logger

def pytest_addoption(parser):

    path = "C:\Program Files\AutomationTestingDrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    parser.addoption("--browser", action="store", default="Chrome",
                     help="Specify the browser name: Chrome, Edge, Firefox or Opera, by default is Chrome")
    parser.addoption("--driver_path", action="store", default=path,
                     help="Specify the driver path, C:./../chromedriver.exe, by default is None")
    parser.addoption("--browser_options", action="store", default=False,
                     help="Specify the browse option as a list, "
                          "ex: --browser_options=[--headless, --window-size=1600,1024, --log-level=0, ... ],"
                          "by default is None")



@pytest.fixture(scope='session')
def driver(request):
    logger.info("Starting the driver: Building the Driver...")
    logger.info("Creating the driver...")
    session_info = SessionInfo(request_config=request.config)
    driver = CustomerDriver(session_info=session_info)
    logger.info(driver._session_info.browser)
    logger.info(', '.join("%s: %s" % item for item in vars(driver).items()))




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