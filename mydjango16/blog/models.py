from django.db import models

class Post(models.Model):  # pk: id (int)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    tag_set = models.ManyToManyField('Tag', blank=True)  # 문자열로 쓰면 서순 이어도 파일 내에서 알아서 찾음
    # manytomany에서는 blank를 왠만하면 써줌
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 인스턴스에 대한 문자열 표현을 기대
    # post.title
    # print(post)
    #

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    # ...
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # post 하나 삭제시 그 post에 달린 comment들을 자동 삭제
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

