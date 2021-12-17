from django.conf import settings
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리 목록"


class Shop(TimestampedModel):
    # settings.AUTH_USER_MODEL 의 디폴트 값 : "auth.User"
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 이게 유저 모델과 외래키 관계를 맺는 가장 정석적인 방법
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)   # 중복 가능, name만으로 검색 가능하도록
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to="shop/shop/%Y/%m/%d")
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "상점"
        verbose_name_plural = "상점 목록"


class Review(TimestampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-id']
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰 목록"


class Tag(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"
