# Generated by Django 4.1.1 on 2022-10-16 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='alias',
            field=models.SlugField(default='demo', unique=True, verbose_name='Alias'),
            preserve_default=False,
        ),
    ]