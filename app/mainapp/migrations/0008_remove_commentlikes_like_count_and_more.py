# Generated by Django 4.1.1 on 2022-11-11 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mainapp", "0007_alter_comment_active_alter_post_active"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="commentlikes",
            name="like_count",
        ),
        migrations.RemoveField(
            model_name="postlikes",
            name="like_count",
        ),
        migrations.AddField(
            model_name="commentlikes",
            name="status",
            field=models.BooleanField(default=True, verbose_name="Статус"),
        ),
        migrations.AddField(
            model_name="postlikes",
            name="status",
            field=models.BooleanField(default=True, verbose_name="Статус"),
        ),
        migrations.AlterField(
            model_name="commentlikes",
            name="comment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment_likes",
                to="mainapp.comment",
                verbose_name="Название статьи",
            ),
        ),
        migrations.AlterField(
            model_name="commentlikes",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment_likes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="postlikes",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_likes",
                to="mainapp.post",
                verbose_name="Название статьи",
            ),
        ),
        migrations.AlterField(
            model_name="postlikes",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_likes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
    ]
