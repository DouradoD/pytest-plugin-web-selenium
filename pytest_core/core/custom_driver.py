import pytest
from selenium.webdriver import Chrome, Firefox, Ie, Safari
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import IEDriverManager
import logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(name)s - %(levelname)s - DRIVER BUILDER - %(message)s",  # Log format
)

logger = logging.getLogger(__name__)
class CustomerDriver:

    def __init__(self, session_info):
        self.session_info = session_info
        self.browser = session_info.browser
        self.webdriver_manager_enabled = session_info.webdriver_manager_enabled
        self._driver = self.generate_driver_by_browser()

    def driver(self, timeout=15):
        self._driver.session_info = self.session_info
        self._driver.wait = WebDriverWait(self._driver, timeout=timeout)
        return self._driver

    def generate_driver_by_browser(self):
        if self.webdriver_manager_enabled:
            logger.info("WebDriverManager is Enabled...")
            if self.browser.lower() == "firefox":
                return Chrome(service=Service(GeckoDriverManager().install()))
            elif self.browser.lower() == "edge":
                return Ie(service=Service(IEDriverManager().install()))
            elif self.browser.lower() == "opera":
                return Safari(service=Service(OperaDriverManager().install()))
            else:
                return Chrome(service=Service(ChromeDriverManager().install()))
        else:
            logger.info("WebDriverManager is Disabled...")
            if self.browser.lower() == "firefox":
                return Firefox(service=Service(self.webdriver_manager_enabled))
            elif self.browser.lower() == "edge":
                return Ie(service=Service(self.webdriver_manager_enabled))
            elif self.browser.lower() == "opera":
                return Safari(service=Service(self.webdriver_manager_enabled))
            else:
                return Chrome(service=Service(self.webdriver_manager_enabled))
