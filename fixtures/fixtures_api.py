import pytest

from api.api_requester import APIRequester
from api.api_requester import api_requester as api_requester_obj


@pytest.fixture(scope='session')
def api_requester() -> APIRequester:
    return api_requester_obj
