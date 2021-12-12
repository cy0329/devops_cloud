from django.core.validators import RegexValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimestampedModel):
    name = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=13,
                                 validators=[RegexValidator(r"^\d{3}-?\d{3,4}-?\d{4}$", message='전화번호를 입력해주세요.'),
                                             ],
                                 help_text="입력 예) 042-123-1234 또는 010-1234-1234")
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    parking = models.BooleanField(default=False)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name


class Review(TimestampedModel):
    shop = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()


class Tag(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

