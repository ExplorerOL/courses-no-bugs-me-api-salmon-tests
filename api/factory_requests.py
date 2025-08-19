from api.post_request import PostRequest
from api.rest.http_session_with_reporting import HTTPSessionWithReporting
from api.rest.rest_request import RESTRequest
from api.validated_post_request import ValidatedPostRequest
from config.config_general import config_general
from config.endpoints import Endpoints


class FactoryRequests:
    @staticmethod
    def __create_http_session() -> HTTPSessionWithReporting:
        return HTTPSessionWithReporting(reporter=config_general.reporter)

    @staticmethod
    def __create_rest_request(
        base_url: str,
    ) -> RESTRequest:
        http_session = FactoryRequests.__create_http_session()
        return RESTRequest(
            base_url=base_url,
            http_session=http_session,
            timeout_ms=config_general.timeout_ms,
        )

    @staticmethod
    def create_post_request(
        base_url: str,
        is_validated: bool = False,
    ) -> PostRequest | ValidatedPostRequest:
        rest_request = FactoryRequests.__create_rest_request(base_url=base_url)
        post_request = PostRequest(rest_request=rest_request, endpoint=Endpoints.POSTS.value)
        if not is_validated:
            return post_request
        return ValidatedPostRequest(post_request=post_request)
