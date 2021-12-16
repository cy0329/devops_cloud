import tablib
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


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


class Post(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)  # db_index는 중복이 있어도 됨, unique는 불가
    content = models.TextField()
    photo = models.ImageField(upload_to="blog/post/%Y/%m/%d")
    tag_set = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(
        max_length=1,
        # FIXME: 장고 3에서 추가된 TextChoices 기능을 활용
        choices=[
            ('D', '초안'),  # DB저장값, Label (Draft==초안)
            ('P', '공개'),  # (Published==공개)
        ],
        db_index=True
    )

    def __str__(self):
        return self.title

    # post_detail 주소 문자열을 반환하길 기대
    # detail 페이지를 구현하자마자, 즉시 아래 메서드를 구현
    def get_absolute_url(self) -> str:
        return reverse('blog:post_detail', args=[self.pk])

    # 이렇게 쓰면 인스턴스 메서드
    # def get_xlsx_data(self):
    #     pass
    @classmethod
    def get_tabular_data(cls, queryset, format="xlsx") -> bytes:
        dataset = tablib.Dataset()
        dataset.headers = ['id', 'title', 'created_at', 'updated_at']
        for post in queryset:
            dataset.append(
                [
                    post.id,
                    post.title,
                    post.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    post.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                ]
            )

        return dataset.export(format)

    class Meta:
        ordering = ['title']


class Comment(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-id']


class Tag(TimestampedModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Subscriber(TimestampedModel):
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                r"^\d{3,4}-?\d{3,4}-?\d{4}$"),
    ]
    )
