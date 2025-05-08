import json
from typing import Any, Dict
from .custom_logger import logger
from .custom_exceptions import MissingArgumentError
class SessionInfo:
    """
    Handles session and capabilities information for the test framework.

    Attributes:
        _request_config: Configuration object for accessing command-line options.
        _session: Dictionary containing session details.
        _capabilities: Dictionary containing browser capabilities.
        _session_info: Combined session and capabilities information.
        _browserOptions: List of browser-specific options.
        _capabilities_path: Path to the capabilities JSON file.
    """

    def __init__(self, request_config):
        self._request_config: Any = request_config
        self._session: Dict[str, str] = {}
        self._capabilities: Dict[str, Any] = {}
        self._session_info: Dict[str, Any] = {}
        self._browserOptions: list = []
        self._capabilities_path: str = request_config.getoption("--capabilities_path")
        self.build_the_session_info()

    @property
    def get_session_info(self) -> Dict[str, Any]:
        return self._session_info
    
    def build_the_session_info(self):
        try:
            self.validate_the_minimum_required()
            if self._capabilities_path:
                self.load_capabilities_from_file()
            else:
                self.load_capabilities_from_args()
        except MissingArgumentError as e:
            logger.error("Failed to build session info: %s", e)
            raise e

    def load_capabilities_from_file(self):
        self._session_info = self.get_json_capabilities()
        logger.info("SessionInfo: %s", self._session_info)
        logger.info("Session: %s", self._session)
        logger.info("Capabilities: %s", self._capabilities)

    def load_capabilities_from_args(self):
        self.get_session_arg()
        self.get_capabilities_arg()
        self.get_browser_options()
        self._capabilities['browserOptions'] = self._browserOptions
        self._session_info = {"session": self._session, "capabilities": self._capabilities}  

    def get_session_arg(self):
        args = self._request_config.getoption("--session").split(" ")
        logger.info("Parsing session arguments: %s", args)
        for arg in args:
             _list = arg.split(":")
             self._session[_list[0]] = _list[1]
        logger.info("Parsed session: %s", self._session)

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
        has_session = self._request_config.getoption("--session")
        has_capabilities = self._request_config.getoption("--capabilities")
        if not self._capabilities_path and not (has_session and has_capabilities):
            raise MissingArgumentError("The --capabilities_path is a required arg WHEN the --session and --capabilities are not provided")

