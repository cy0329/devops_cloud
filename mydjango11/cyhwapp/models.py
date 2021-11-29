from django.db import models

class Badmintonplace(models.Model):
    name = models.CharField(max_length=50, verbose_name='이름')
    address = models.CharField(max_length=100, verbose_name='주소')
    phone_num = models.CharField(max_length=11, verbose_name='연락처')
    homepage = models.CharField(max_length=200, verbose_name='홈페이지')
    email = models.CharField(max_length=50, verbose_name='이메일')


    def __str__(self):
        return self.name