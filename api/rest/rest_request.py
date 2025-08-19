import requests

from api.rest.http_session_with_reporting import HTTPSessionWithReporting


class RESTRequest:
    def __init__(self, base_url: str, http_session: HTTPSessionWithReporting, timeout_ms: int = 10000):
        self.__base_url = base_url
        self.__timeput_ms = timeout_ms
        self.__session = http_session

    @property
    def base_url(self) -> str:
        return self.__base_url

    @property
    def session(self) -> requests.Session:
        return self.__session

    @property
    def timeout_ms(self) -> int:
        return self.__timeput_ms
