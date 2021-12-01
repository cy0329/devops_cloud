from django.db import models

class Resort(models.Model):
    place_name = models.CharField(max_length=100, verbose_name='스키장 이름')
    address = models.CharField(max_length=100, verbose_name='주소')
    contact = models.CharField(max_length=13, blank=True, verbose_name='연락처')
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정')
