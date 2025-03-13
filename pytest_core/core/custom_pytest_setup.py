import pytest
from core.session_info import SessionInfo
from core.custom_driver import CustomerDriver
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(name)s - %(levelname)s - Conftest - %(message)s",  # Log format
)

logger = logging.getLogger(__name__)

def pytest_addoption(parser):

    path = "C:\Program Files\AutomationTestingDrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    parser.addoption("--browser", action="store", default="Chrome",
                     help="Specify the browser name: Chrome, Edge, Firefox or Opera, by default is Chrome")
    parser.addoption("--webdriver_manager_enabled", action="store", default=False,
                     help="Specify True to use the webdriver_manager, by default is False")
    parser.addoption("--driver_path", action="store", default=path,
                     help="Specify the driver path, C:./../chromedriver.exe, by default is None")
    parser.addoption("--headless", action="store", default=False,
                     help="Specify the headless value, by default is False")



@pytest.fixture(scope='session')
def driver(request):
    logger.info("Starting the driver: Building the Driver...")
    logger.info("Creating the driver...")
    session_info = SessionInfo(request_config=request.config)
    custom_driver = CustomerDriver(session_info=session_info)
    logger.info(custom_driver.browser)
    logger.info(custom_driver.webdriver_manager_enabled)
    logger.info(', '.join("%s: %s" % item for item in vars(custom_driver).items()))




    driver = custom_driver.driver(timeout=15)
    driver.maximize_window()


    logger.info("The pytest_with_core_plugin are going to run...")
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