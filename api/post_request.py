import json
from dataclasses import asdict

from requests import Response

from api.endpoint import Endpoint
from api.interfaces.crud_interface import CRUDInterface
from api.interfaces.read_all_interface import ReadAllInterface
from api.rest.rest_request import RESTRequest
from models.post import Post


class PostRequest(CRUDInterface, ReadAllInterface):
    def __init__(self, rest_request: RESTRequest, endpoint: Endpoint):
        self.__rest_request = rest_request
        self.__endpoint = str(endpoint)

    def create(self, data: Post) -> Response:
        """Отправка запроса на создание"""
        response = self.__rest_request.session.post(
            self.__rest_request.base_url + str(self.__endpoint),
            json=asdict(data),
            headers={'Content-Type': 'application/json'},
            verify=False,
            timeout=self.__rest_request.timeout_ms / 1000,
        )
        return response

    def update(self, id, data: Post) -> Response:
        """Отправка запроса на обновление"""
        response = self.__rest_request.session.put(
            url=self.__rest_request.base_url + self.__endpoint + '/' + str(id),
            data=json.dumps(asdict(data)),
            headers={'Content-Type': 'application/json'},
            verify=False,
            timeout=self.__rest_request.timeout_ms / 1000,
        )
        return response

    def delete(self, id: int) -> Response:
        """Отправка запроса на удаление"""
        response = self.__rest_request.session.delete(
            url=self.__rest_request.base_url + self.__endpoint + '/' + str(id),
            verify=False,
            timeout=self.__rest_request.timeout_ms / 1000,
        )
        return response

    def read(self, id: int, user_id: int | None = None) -> Response:
        """Отправка запроса на чтение одной записи"""
        params = {}
        if user_id:
            params = {'userId': user_id}
        response = self.__rest_request.session.get(
            self.__rest_request.base_url + self.__endpoint + '/' + str(id),
            params=params,
            verify=False,
            timeout=self.__rest_request.timeout_ms / 1000,
        )
        return response

    def read_by_user_id(self, user_id: int) -> Response:
        """Отправка запроса на чтение записей по userId"""
        params = {'userId': user_id}
        response = self.__rest_request.session.get(
            self.__rest_request.base_url + self.__endpoint,
            params=params,
            verify=False,
            timeout=self.__rest_request.timeout_ms / 1000,
        )
        return response

    def read_all(self) -> Response:
        """Отправка запроса на чтение всех записей"""
        response = self.__rest_request.session.get(
            self.__rest_request.base_url + self.__endpoint,
            verify=False,
            timeout=self.__rest_request.timeout_ms / 1000,
        )
        return response
