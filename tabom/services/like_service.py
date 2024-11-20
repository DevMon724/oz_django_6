from django.db.models import F

from tabom.models import Article, Like

# def do_like(user_id: int, article_id: int) -> Like:
#     return Like.objects.create(user_id=user_id, article_id=article_id)


# 동시성 문제 해결을 위해 F expre
def do_like(user_id: int, article_id: int) -> Like:
    # article = Article.objects.get(id=article_id)
    like = Like.objects.create(user_id=user_id, article_id=article_id)
    Article.objects.filter(id=article_id).update(like_count=F("like_count") + 1)
    # article.like_count += 1
    # article.save()
    return like


def undo_like(user_id: int, article_id: int) -> None:
    deleted_cnt, _ = Like.objects.filter(user_id=user_id, article_id=article_id).delete()
    if deleted_cnt:
        article = Article.objects.filter(id=article_id).get()
        article.like_count -= 1
        article.save()
