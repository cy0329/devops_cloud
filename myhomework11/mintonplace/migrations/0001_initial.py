# Generated by Django 3.2.9 on 2021-11-30 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mintongym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100, verbose_name='민턴장 이름')),
                ('address', models.CharField(max_length=100, verbose_name='주소')),
                ('contact', models.IntegerField(verbose_name='연락처')),
                ('parking', models.BooleanField(verbose_name='주차장 보유')),
                ('running_time', models.TextField(verbose_name='운영시간 및 설명')),
            ],
        ),
    ]
