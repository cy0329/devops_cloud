# Generated by Django 3.2.9 on 2021-12-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mintonplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='parking',
            field=models.BooleanField(default=False, verbose_name='주차장 보유'),
        ),
    ]
