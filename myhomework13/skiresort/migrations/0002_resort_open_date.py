# Generated by Django 3.2.9 on 2021-12-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skiresort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resort',
            name='open_date',
            field=models.DateField(auto_now=True, verbose_name='개장일'),
        ),
    ]
