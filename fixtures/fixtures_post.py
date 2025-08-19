import random

import pytest

from api.api_requester import APIRequester
from fixtures.fixtures_general import test_app_before_testrun  # noqa
from models.post import Post
from support.generators.generators_entity import GeneratorsEntity


@pytest.fixture(scope='function')
def random_existed_post_scope_test(api_requester: APIRequester) -> Post:
    actual_posts = api_requester.validated_post_request_anonim.read_all()
    return random.choice(actual_posts)


@pytest.fixture(scope='function')
def random_data_post_scope_test() -> Post:
    return GeneratorsEntity.generate_entity_with_random_data(entity_type=Post)


@pytest.fixture(scope='function')
def actual_posts_max_id(api_requester: APIRequester) -> int:
    actual_posts = api_requester.validated_post_request_anonim.read_all()
    return max(actual_posts, key=lambda post: post.id).id


@pytest.fixture(scope='function')
def delete_all_posts_before_test_scope_test(api_requester: APIRequester) -> None:
    api_requester.validated_post_request_anonim.delete_all()
