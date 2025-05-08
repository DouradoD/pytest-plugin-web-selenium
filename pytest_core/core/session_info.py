import json
from .custom_logger import logger
class SessionInfo:

    def __init__(self, request_config):
        self._request_config = request_config
        self._session = {}
        self._capabilities = {}
        self._session_info = {}
        self._browserOptions = []
        self._capabilities_path = request_config.getoption("--capabilities_path")
        self.build_the_session_info()

    @property
    def get_session_info(self):
        return self._session_info
    
    def build_the_session_info(self):
        self.validate_the_minimum_required()
        if self._capabilities_path:
            self._session_info = self.get_json_capabilities()
            logger.info("SessionInfo: %s", self._session_info)
            logger.info("Session: %s", self._session)
            logger.info("Capabilities: %s", self._capabilities)
        else:
            self.get_session_arg()
            self.get_capabilities_arg()
            self.get_browser_options()
            self._capabilities['browserOptions']= self._browserOptions
            self._session_info = {"session": self._session, "capabilities": self._capabilities}   

    def get_session_arg(self):
         args = self._request_config.getoption("--session").split(" ")
         for arg in args:
             _list = arg.split(":")
             self._session[_list[0]] = _list[1]

    def get_capabilities_arg(self):
         args = self._request_config.getoption("--capabilities").split(" ")
         for arg in args:
             _list = arg.split(":")
             self._capabilities[_list[0]] = _list[1]

    def get_browser_options(self):
        args = self._request_config.getoption("--browserOptions").strip("[]")
        self._browserOptions = args.split(" ")
    
    def get_json_capabilities(self):
        with open(self._capabilities_path, 'r') as file:
            return json.load(file)

    def validate_the_minimum_required(self):
        if self._capabilities_path:
            pass
        elif self._request_config.getoption("--session") and self._request_config.getoption("--capabilities"):
            pass
        else:
            raise Exception("The --capabilities_path is a required arg WHEN the --session and --capabilities are not provided")


