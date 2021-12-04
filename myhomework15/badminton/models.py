from django.db import models
from django.core.validators import RegexValidator

class Minton(models.Model):
    name = models.CharField(max_length=50, verbose_name='민턴장 이름')
    address = models.CharField(max_length=200, verbose_name='주소')
    telephone = models.CharField(blank=True, max_length=15, validators=[
        RegexValidator(r"^\d{3,4}-?\d{3,4}-?\d{4}$",
                       message="전화번호를 입력해주세요."),
    ])
    photo = models.ImageField(blank=True, verbose_name='사진')
    description = models.TextField(verbose_name='설명')
    parking = models.BooleanField(default=False, verbose_name='주차장 보유')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
