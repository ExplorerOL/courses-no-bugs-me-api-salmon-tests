import pytest

from api.api_requester import APIRequester
from api.response_validators.api_response_validators_templates import APIResponseValidatorsTemplates
from models.post import Post
from support.base_test import BaseTest


@pytest.mark.usefixtures('delete_all_posts_before_test_scope_test')
class TestPostsDelete(BaseTest):
    def test_delete_post(
        self,
        api_requester: APIRequester,
        random_existed_post_scope_test: Post,
    ):
        """Удаление поста"""
        with self.ACT():
            api_requester.validated_post_request_anonim.delete(id=random_existed_post_scope_test.id)


@pytest.mark.usefixtures('delete_all_posts_before_test_scope_test')
class TestPostsDeleteNegative(BaseTest):
    def test_delete_post_with_non_existent_id(
        self,
        api_requester: APIRequester,
        actual_posts_max_id: int,
    ):
        """Удаление поста c несуществующим id"""
        with self.ARRANGE():
            post_id_for_deletion = actual_posts_max_id + 1
        with self.ACT():
            api_requester.validated_post_request_anonim.delete(
                id=post_id_for_deletion,
                response_validator=APIResponseValidatorsTemplates.status_ok_body_curly_brakets,
            )
