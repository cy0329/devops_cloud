from django.db import migrations, models

# 절대 상단에서 from shop.models import Category를 하지 말고
# 마이그레이션 함수 내부에서 apps 를 통해 모델 클래스를 가져오세요.


def create_dummy_category(apps, schema_editor):
    Category = apps.get_model("shop", "Category")  # model class
    Category.objects.create(name="dummy")   # pk: 1


def delete_dummy_category(apps, schema_editor):
    Category = apps.get_model("shop", "Category")  # model class
    Category.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(create_dummy_category, delete_dummy_category)
    ]
