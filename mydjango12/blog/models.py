from django.db import models
from blog.upload_to import uuid_name_upload_to

class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # upload_to
    #  - 문자열 : 파일이 저장되는 폴더의 경로
    #photo = models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d/%H') # 파일 찾는 성능 최적화를 위한 경로 지정
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)  # 등록한 시각 자동 지정
    updated_at = models.DateTimeField(auto_now=True)  # 수정한 시각 자동 지정
