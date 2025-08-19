import pytest

from api.api_requester import APIRequester
from models.post import Post
from support.base_test import BaseTest


@pytest.mark.usefixtures('delete_all_posts_before_test_scope_test')
class TestPostsCreate(BaseTest):
    def test_create_post(
        self,
        api_requester: APIRequester,
        random_data_post_scope_test: Post,
        actual_posts_max_id: int,
    ):
        """Создание поста"""
        with self.ARRANGE():
            random_data_post_scope_test.id = actual_posts_max_id + 1
        with self.ACT():
            actual_post = api_requester.validated_post_request_anonim.create(data=random_data_post_scope_test)
        with self.ASSERT(msg='Проверка данных созданного поста'):
            self.assertions.verify_is_equal(
                actual_value=actual_post,
                expected_value=random_data_post_scope_test,
            )

    def test_create_post_with_empty_title(
        self,
        api_requester: APIRequester,
        random_data_post_scope_test: Post,
        actual_posts_max_id: int,
    ):
        """Создание поста с пустым заголовком"""
        with self.ARRANGE():
            random_data_post_scope_test.title = ''
            random_data_post_scope_test.id = actual_posts_max_id + 1
        with self.ACT():
            actual_post = api_requester.validated_post_request_anonim.create(data=random_data_post_scope_test)
        with self.ASSERT(msg='Проверка данных созданного поста'):
            self.assertions.verify_is_equal(
                actual_value=actual_post,
                expected_value=random_data_post_scope_test,
            )

    def test_create_post_with_empty_body(
        self,
        api_requester: APIRequester,
        random_data_post_scope_test: Post,
        actual_posts_max_id: int,
    ):
        """Создание поста с пустым содержанием"""
        with self.ARRANGE():
            random_data_post_scope_test.body = ''
            random_data_post_scope_test.id = actual_posts_max_id + 1
        with self.ACT():
            actual_post = api_requester.validated_post_request_anonim.create(data=random_data_post_scope_test)
        with self.ASSERT(msg='Проверка данных созданного поста'):
            self.assertions.verify_is_equal(
                actual_value=actual_post,
                expected_value=random_data_post_scope_test,
            )
