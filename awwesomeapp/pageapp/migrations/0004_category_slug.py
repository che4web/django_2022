# Generated by Django 3.2 on 2022-11-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pageapp', '0003_page_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='news', unique=True),
            preserve_default=False,
        ),
    ]
