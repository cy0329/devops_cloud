from django.db import models
from django.core.validators import MinLengthValidator


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 추상 클래스로서, DB 테이블이 생기지 않음


class Post(TimestampedModel):  # 상속 받아서 정의 --> 코드 줄이기
    author_name = models.CharField(max_length=20)
    title = models.CharField(
        max_length=200,
        db_index=True,
        validators=[
            MinLengthValidator(3),
            # MaxLengthValidator() 는 이미 위에 max_length가 있어서 넣을 필요 없음
        ],
    )
    content = models.TextField()
    photo = models.ImageField(upload_to="diary/post/%Y/%m/%d")
    tag_set = models.ManyToManyField("Tag", blank=True)
    ip = models.GenericIPAddressField()

    # Tag가 뒤에 있기 때문에 문자열로 넣어주면 장고가 알아서 현재 앱에서 찾아서 관계를 맺어줌
    def __str__(self) -> str:
        return f"[{self.pk}] {self.title}"

    class Meta:
        verbose_name = "포스팅"
        verbose_name_plural = "포스팅 목록"


class Comment(TimestampedModel):
    # 외래키 : 정수값
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # on_delete : 삭제 정책 -> CASCADE : Post 삭제시 포함된 Comment도 삭제
    # post_id라는 필드를 자동으로 생성(by django)
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"


class Tag(TimestampedModel):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"
