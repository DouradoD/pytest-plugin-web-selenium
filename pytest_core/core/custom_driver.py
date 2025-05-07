
from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions, Safari, SafariOptions, Edge, EdgeOptions
from selenium.webdriver.support.wait import WebDriverWait

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
        self._driver = self.get_browser()

    def driver(self, timeout=15):
        self._driver.session_info = self.session_info
        self._driver.wait = WebDriverWait(self._driver, timeout=timeout)
        return self._driver

    def get_browser(self):
        if self.browser.lower() == "firefox":
            return Firefox(options=self.get_browser_options())
        elif self.browser.lower() == "edge":
            return Edge(options=self.get_browser_options())
        elif self.browser.lower() == "opera":
            return Safari(options=self.get_browser_options())
        else:
            return Chrome(options=self.get_browser_options())

    def get_browser_options(self):
        if self.browser.lower() == "firefox":
            obj_option = FirefoxOptions()
        elif self.browser.lower() == "edge":
            obj_option = EdgeOptions()
        elif self.browser.lower() == "opera":
            obj_option = SafariOptions()
        else:
            obj_option = ChromeOptions()
        # WIP - Add more options for each browser
        return obj_option
