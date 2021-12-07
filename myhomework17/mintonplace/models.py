from django.db import models
from django.core.validators import RegexValidator


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimestampedModel):
    name = models.CharField(max_length=50, verbose_name="민턴장 이름", db_index=True)
    address = models.CharField(max_length=100, verbose_name="주소")
    telephone = models.CharField(max_length=15,
                                 validators=[
                                     RegexValidator(
                                         r"^\d{3,4}-?\d{3,4}-?\d{4}$", message="전화번호를 입력해주세요."
                                     )
                                 ]
                                 )
    photo = models.ImageField(blank=True, verbose_name="사진")
    description = models.TextField(blank=True, verbose_name="설명")
    parking = models.BooleanField(default=False, verbose_name="주차장 보유")
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "포스팅"
        verbose_name_plural = "포스팅 목록"


class Comment(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"


class Tag(TimestampedModel):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name
