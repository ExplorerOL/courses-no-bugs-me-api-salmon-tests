from enum import Enum, StrEnum

from api.endpoint import Endpoint
from config.config_general import config_general


class EndpointsVersions(StrEnum):
    MOBILE = ''
    WEB = ''


class Endpoints(Enum):
    POSTS = Endpoint(
        enpoint='/posts',
        version_or_get_version_func=config_general.get_api_version,
    )
