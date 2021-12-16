from django.core.validators import RegexValidator
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


class Shop(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=15,
                                 validators=[
                                     RegexValidator(r"^\d{3,4}-?\d{3,4}-?\d{4}$", message="전화번호를 입력하세요."), ])
    description = models.TextField()
    photo = models.ImageField(upload_to="shop/post/%Y/%m/%d")
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Tag(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Review(TimestampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-id']
