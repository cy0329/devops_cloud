# Generated by Django 3.2.9 on 2021-12-04 14:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Minton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='민턴장 이름')),
                ('address', models.CharField(max_length=200, verbose_name='주소')),
                ('telephone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^\\d{3,4}-?\\d{3,4}-?\\d{4}$', message='전화번호를 입력해주세요.')])),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='사진')),
                ('description', models.TextField(verbose_name='설명')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
