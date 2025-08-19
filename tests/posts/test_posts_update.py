import pytest

from api.api_requester import APIRequester
from api.response_validators.api_response_validators_templates import APIResponseValidatorsTemplates
from models.post import Post
from support.base_test import BaseTest


@pytest.mark.usefixtures('delete_all_posts_before_test_scope_test')
class TestPostsUpdate(BaseTest):
    def test_update_post(
        self,
        api_requester: APIRequester,
        random_existed_post_scope_test: Post,
        random_data_post_scope_test: Post,
    ):
        """Обновление поста"""
        with self.ARRANGE():
            random_data_post_scope_test.id = random_existed_post_scope_test.id
        with self.ACT():
            actual_post = api_requester.validated_post_request_anonim.update(
                id=random_existed_post_scope_test.id,
                data=random_data_post_scope_test,
            )
        with self.ASSERT(msg='Проверка данных созданного поста'):
            self.assertions.verify_is_equal(
                actual_value=actual_post,
                expected_value=random_data_post_scope_test,
            )


@pytest.mark.usefixtures('delete_all_posts_before_test_scope_test')
class TestPostsUpdateNegative(BaseTest):
    def test_update_post_with_non_existent_id(
        self,
        api_requester: APIRequester,
        actual_posts_max_id: int,
        random_data_post_scope_test: Post,
    ):
        """Обновление поста с несуществующим id"""
        with self.ARRANGE():
            post_id_for_updating = actual_posts_max_id + 1
        with self.ACT():
            api_requester.validated_post_request_anonim.update(
                id=post_id_for_updating,
                data=random_data_post_scope_test,
                response_validator=APIResponseValidatorsTemplates.staus_not_found,
            )
