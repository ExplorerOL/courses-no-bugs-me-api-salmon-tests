from typing import Iterable

from models.post import Post
from support.reporters.allure.reporting_classes import ClassWithMethodReporting


class OperationsPosts(ClassWithMethodReporting):
    @staticmethod
    def filter_posts_by_user_id(user_id: int, posts: Iterable[Post], sort_by_id: bool = False) -> list[Post]:
        """Фильтрация постов по id пользователя"""
        user_posts = list(filter(lambda x: x.userId == user_id, posts))
        if sort_by_id:
            user_posts = sorted(
                user_posts,
                key=lambda elem: elem.id,
            )
        return user_posts
