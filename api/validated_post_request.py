import http

from api.interfaces.crud_interface import CRUDInterface
from api.interfaces.read_all_interface import ReadAllInterface
from api.post_request import PostRequest
from api.response_validators.api_response_validator import APIResponseValidator
from api.response_validators.api_response_validators_templates import APIResponseValidatorsTemplates
from models.post import Post


class ValidatedPostRequest(CRUDInterface, ReadAllInterface):
    def __init__(self, post_request: PostRequest):
        self.__post_request = post_request

    def create(
        self,
        data: Post,
        response_validator: APIResponseValidator = APIResponseValidatorsTemplates.status_created,
        soft_validation: bool = False,
    ) -> Post:
        """Отправка запроса на создание с валидацией ответа"""
        response = self.__post_request.create(data=data)
        response_validator.validate_response(response=response, soft=soft_validation)
        body_json = response.json()
        return Post(**body_json)

    def update(
        self,
        id: int,
        data: Post,
        response_validator: APIResponseValidator = APIResponseValidatorsTemplates.status_ok,
        soft_validation: bool = False,
    ) -> Post:
        """Отправка запроса на обновление с валидацией ответа"""
        response = self.__post_request.update(id=id, data=data)
        response_validator.validate_response(response=response, soft=soft_validation)
        body_json = response.json()
        return Post(**body_json)

    def delete(
        self,
        id: int,
        response_validator: APIResponseValidator = APIResponseValidatorsTemplates.status_ok_body_curly_brakets,
        soft_validation: bool = False,
    ) -> str:
        """Отправка запроса на удаление с валидацией ответа"""
        response = self.__post_request.delete(id=id)
        response_validator.validate_response(response=response, soft=soft_validation)
        return response.text

    def delete_all(self) -> None:
        """Удаление всех записей"""
        existed_posts = self.read_all()
        for post in existed_posts:
            self.delete(id=post.id)

    def read(
        self,
        id: int,
        response_validator: APIResponseValidator = APIResponseValidatorsTemplates.status_ok,
        soft_validation: bool = False,
    ) -> Post | None:
        """Отправка запроса на чтение одной сущности с валидацией ответа"""
        response = self.__post_request.read(id=id)
        response_validator.validate_response(response=response, soft=soft_validation)
        if response.status_code == http.HTTPStatus.NOT_FOUND:
            return None
        body_json = response.json()
        return Post(**body_json)

    def read_all_by_user_id(
        self,
        user_id: int,
        response_validator: APIResponseValidator = APIResponseValidatorsTemplates.status_ok,
        soft_validation: bool = False,
    ) -> list[Post]:
        """Отправка запроса на чтение всех сущностей пользовтеля с валидацией ответа"""
        response = self.__post_request.read_by_user_id(user_id=user_id)
        response_validator.validate_response(response=response, soft=soft_validation)
        body_json = response.json()
        return [Post(**post) for post in body_json]

    def read_all(
        self,
        response_validator: APIResponseValidator = APIResponseValidatorsTemplates.status_ok,
        soft_validation: bool = False,
    ) -> list[Post]:
        """Отправка запроса на чтение всех сущностей с валидацией ответа"""
        response = self.__post_request.read_all()
        response_validator.validate_response(response=response, soft=soft_validation)
        body_json = response.json()
        return [Post(**post) for post in body_json]
