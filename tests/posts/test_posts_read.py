import pytest

from api.api_requester import APIRequester
from api.response_validators.api_response_validators_templates import APIResponseValidatorsTemplates
from models.post import Post
from support.base_test import BaseTest


@pytest.mark.usefixtures('delete_all_posts_before_test_scope_test')
class TestPostsRead(BaseTest):
    def test_read_all_posts(
        self,
        api_requester: APIRequester,
    ):
        """Чтение всех постов"""
        with self.ARRANGE():
            EXPECTED_POSTS_COUNT = 100
        with self.ACT():
            posts = api_requester.validated_post_request_anonim.read_all()
        with self.ASSERT():
            self.assertions.verify_is_equal(
                actual_value=len(posts),
                expected_value=EXPECTED_POSTS_COUNT,
            )

    def test_read_post(
        self,
        api_requester: APIRequester,
        random_existed_post_scope_test: Post,
    ):
        """Чтение поста"""
        with self.ACT():
            actual_post = api_requester.validated_post_request_anonim.read(
                id=random_existed_post_scope_test.id
            )
        with self.ASSERT(msg='Проверка данных прочитанного поста'):
            self.assertions.verify_is_equal(
                actual_value=actual_post,
                expected_value=random_existed_post_scope_test,
            )

    def test_read_all_posts_by_user(
        self,
        api_requester: APIRequester,
        random_existed_post_scope_test: Post,
    ):
        """Чтение всех постов пользователя"""
        with self.ARRANGE():
            all_actual_posts = api_requester.validated_post_request_anonim.read_all()
            expected_user_posts = self.operations_posts.filter_posts_by_user_id(
                user_id=random_existed_post_scope_test.userId,
                posts=all_actual_posts,
                sort_by_id=True,
            )
        with self.ACT():
            actual_user_posts = api_requester.validated_post_request_anonim.read_all_by_user_id(
                user_id=random_existed_post_scope_test.userId,
            )
        with self.ASSERT(msg='Проверка данных постов пользователя'):
            self.assertions.verify_is_equal(
                actual_value=actual_user_posts,
                expected_value=expected_user_posts,
            )


@pytest.mark.usefixtures('delete_all_posts_before_test_scope_test')
class TestPostsReadNegative(BaseTest):
    def test_read_post_with_non_existent_id(
        self,
        api_requester: APIRequester,
        actual_posts_max_id: int,
    ):
        """Чтение поста с несуществующим id"""
        with self.ARRANGE():
            post_id_for_reading = actual_posts_max_id + 1
        with self.ACT():
            api_requester.validated_post_request_anonim.read(
                id=post_id_for_reading,
                response_validator=APIResponseValidatorsTemplates.status_not_found_body_curly_brackets,
            )
