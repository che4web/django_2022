# Generated by Django 3.2 on 2022-11-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pageapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='1', unique=True),
            preserve_default=False,
        ),
    ]
