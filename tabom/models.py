from django.db import models

# Create your models here.


# 상속클래스이기 때문에 데이터베이스 모델에는 변경사항 없어서 migration 되지 않음.
class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=50)


class Article(BaseModel):
    title = models.CharField(max_length=255)


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
