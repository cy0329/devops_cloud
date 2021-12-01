# Generated by Django 3.2.9 on 2021-12-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100, verbose_name='스키장 이름')),
                ('address', models.CharField(max_length=100, verbose_name='주소')),
                ('contact', models.CharField(blank=True, max_length=13, verbose_name='연락처')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정')),
            ],
        ),
    ]
