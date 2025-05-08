
from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions, Safari, SafariOptions, Edge, EdgeOptions
from selenium.webdriver.support.wait import WebDriverWait

from .custom_logger import logger
class CustomerDriver:

    def __init__(self, session_info):
        self._session_info = session_info
        self._driver = self.build_driver()
        self.inject_custom_info_on_driver()
        self._driver.logger.info("Driver is built and ready to use.")

    def driver(self, timeout=15):
        self._driver.wait = WebDriverWait(self._driver, timeout=timeout)
        return self._driver
    
    def inject_custom_info_on_driver(self):
        self._driver.session_info = self._session_info
        self._driver.logger = logger

    def build_driver(self):
        browser = self._session_info['capabilities']['browserName']
        if browser == "firefox":
            return Firefox(options=self.get_browser_options(browser))
        elif browser == "edge":
            return Edge(options=self.get_browser_options(browser))
        elif browser == "opera":
            return Safari(options=self.get_browser_options(browser))
        else:
            return Chrome(options=self.get_browser_options(browser))

    def get_browser_options(self, browser):
        if browser == "firefox":
            obj_option = FirefoxOptions()
        elif browser == "edge":
            obj_option = EdgeOptions()
        elif browser == "opera":
            obj_option = SafariOptions()
        else:
            obj_option = ChromeOptions()
        for arg in self._session_info['capabilities']['browserOptions']:
            obj_option.add_argument(arg)
        return obj_option
