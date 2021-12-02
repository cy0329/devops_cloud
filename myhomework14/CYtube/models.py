from django.db import models

class CYvlog(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    description = models.TextField(verbose_name='설명')
    video_file = models.FileField(verbose_name='동영상')
    thumbnail_file = models.ImageField(verbose_name='썸네일')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)