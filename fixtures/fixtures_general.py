import pytest

from api.api_requester import APIRequester


@pytest.fixture(scope='session')
def test_app_before_testrun(api_requester: APIRequester):
    try:
        api_requester.validated_post_request_anonim.read_all()
    except Exception as error:
        pytest.exit(reason=f'Тестовое приложение не доступно. Возникла ошибка {error}')
