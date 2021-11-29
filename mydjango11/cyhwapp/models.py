from django.db import models

class Badmintonplace(models.Model):
    name = models.CharField(max_length=50, verbose_name='이름')
    address = models.CharField(max_length=100, verbose_name='주소')
    phone_num = models.CharField(max_length=11, verbose_name='연락처')
    homepage = models.CharField(max_length=200, verbose_name='홈페이지', blank=True, null=True)
    email = models.CharField(max_length=50, verbose_name='이메일', blank=True, null=True)
    parking = models.BooleanField(verbose_name='주차장 보유 여부')


    def __str__(self):
        return self.name