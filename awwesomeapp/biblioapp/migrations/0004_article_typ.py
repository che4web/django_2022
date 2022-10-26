# Generated by Django 3.2 on 2022-10-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioapp', '0003_article_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='typ',
            field=models.CharField(choices=[('AR', 'Статья  в журнале'), ('BK', 'Книга')], default='AR', max_length=2),
        ),
    ]