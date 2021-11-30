from django.db import models
from mintonplace.upload_to import uuid_name_upload_to
import datetime

class mintongym(models.Model):
    place_name = models.CharField(max_length=100, verbose_name='민턴장 이름')
    address = models.CharField(max_length=100, verbose_name='주소')
    contact = models.CharField(max_length=11, verbose_name='연락처', blank=True)
    parking = models.BooleanField(verbose_name='주차장 보유')
    starttime = models.TimeField(verbose_name='시작 시간', default=datetime.time(), blank=True)
    endtime = models.TimeField(verbose_name='종료 시간', default=datetime.time(), blank=True)
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    explain = models.TextField(verbose_name='설명', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 등록한 시각 자동 지정
    updated_at = models.DateTimeField(auto_now=True)  # 수정한 시각 자동 지정

    def __str__(self):
        return self.place_name