from django.db import models

class mintongym(models.Model):
    place_name = models.CharField(max_length=100, verbose_name='민턴장 이름')
    address = models.CharField(max_length=100, verbose_name='주소')
    contact = models.IntegerField(verbose_name='연락처')
    parking = models.BooleanField(verbose_name='주차장 보유')
    running_time = models.TextField(verbose_name='운영시간 및 설명')
