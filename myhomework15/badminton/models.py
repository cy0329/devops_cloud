from django.db import models

class Minton(models.Model):
    name = models.CharField(max_length=50, verbose_name="체육관명")
    description = models.TextField(verbose_name="설명")
    photo = models.ImageField(verbose_name="사진", blank=True)
    # open_at = models.TimeField(auto_now=True)
    parking = models.BooleanField(blank=True, verbose_name="주차장 보유")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

