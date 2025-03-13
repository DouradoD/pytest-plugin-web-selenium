class SessionInfo:

    def __init__(self, request_config):
        self.browser = request_config.getoption("--browser")
        self.webdriver_manager_enabled = request_config.getoption("--webdriver_manager_enabled")
        self.driver_path = request_config.getoption("--driver_path")