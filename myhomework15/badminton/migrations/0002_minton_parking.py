# Generated by Django 3.2.9 on 2021-12-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badminton', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='minton',
            name='parking',
            field=models.BooleanField(default=False, verbose_name='주차장 보유'),
        ),
    ]
