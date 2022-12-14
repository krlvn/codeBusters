# Generated by Django 4.1.1 on 2022-10-31 07:20

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_post_image"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="post",
            managers=[
                ("objects_all", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True,
                max_length=150,
                null=True,
                upload_to="post_image",
                verbose_name="Главное изображение статьи",
            ),
        ),
    ]
