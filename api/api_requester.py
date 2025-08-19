from api.factory_requests import FactoryRequests
from api.post_request import PostRequest
from api.validated_post_request import ValidatedPostRequest
from config.config_general import config_general


class APIRequester:
    def __init__(
        self,
        base_url: str,
    ):
        self.__post_request_anonim = FactoryRequests.create_post_request(
            base_url=base_url,
            is_validated=False,
        )
        self.__validated_post_request_anonim = FactoryRequests.create_post_request(
            base_url=base_url,
            is_validated=True,
        )

    @property
    def post_request_anonim(self) -> PostRequest:
        return self.__post_request_anonim

    @property
    def validated_post_request_anonim(self) -> ValidatedPostRequest:
        return self.__validated_post_request_anonim


api_requester = APIRequester(
    base_url=config_general.base_url,
)
