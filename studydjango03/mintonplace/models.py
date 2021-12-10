from django.core.validators import RegexValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimestampedModel):
    name = models.CharField(max_length=50, db_index=True, verbose_name='민턴장 이름')
    address = models.CharField(max_length=100, verbose_name='주소')
    telephone = models.CharField(max_length=15, verbose_name='전화번호', validators=[
        RegexValidator(r"^\d{3,4}-?\d{3,4}-?\d{4}$", message='전화번호를 입력해주세요.'), ])
    description = models.TextField(verbose_name="설명", blank=True)
    photo = models.ImageField(blank=True, verbose_name='사진')
    parking = models.BooleanField(default=False, verbose_name="주차장 보유")
    tag_set = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '포스팅'
        verbose_name_plural = '포스팅 목록'


class Comment(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=30, verbose_name='글쓴이')
    message = models.TextField(verbose_name='댓글')

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글 목록'


class Tag(TimestampedModel):
    name = models.CharField(max_length=50, verbose_name='태그', db_index=True)

    def __str__(self):
        return self.name


