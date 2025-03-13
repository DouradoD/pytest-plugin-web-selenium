import pytest
from pytest_core.session_info import SessionInfo
from pytest_core.custom_driver import CustomerDriver

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
    session_info = SessionInfo(request_config=request.config)
    custom_driver = CustomerDriver(session_info=session_info)
    driver = custom_driver.driver(timeout=15)
    driver.maximize_window()
    print('Finished to create the driver!')

    print('The pytest_with_core_plugin are going to run ....')
    yield driver

    print('Finishing the Driver/Tests')
    driver.quit()


def pytest_report_teststatus(report):
    if report.when == "call" and report.passed:
        return "✅ ", "PASS", "PASSED"
    else:
        return "❌ ", "FAIL", "FAILED"