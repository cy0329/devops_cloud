from django.core.validators import RegexValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Shop(TimestampedModel):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    telephone = models.CharField(max_length=13,
                                 validators=[RegexValidator(r"^\d{3}-?\d{3,4}-?\d{4}$", message='전화번호를 입력해주세요.'),
                                             ],
                                 help_text="입력 예) 042-123-1234 또는 010-1234-1234")
    tag_set = models.ManyToManyField('Tag', blank=True)  # 태그를 꼭 써주겠다 하면 blank를 빼주거나 False로


class Review(TimestampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()


class Tag(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)  # 유일성
