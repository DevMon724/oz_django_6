from django.test import TestCase

from tabom.models import Article, User
from tabom.sevices.like_service import do_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # when
        like = do_like(user.id, article.id)

        # then
        # id 가 들어있다는 것은 데이터베이스로부터 id를 발급받았다는 뜻
        # 즉, 성공적으로 Insert가 되었다는 뜻.
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)
