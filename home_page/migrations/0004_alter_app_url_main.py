# Generated by Django 4.2.5 on 2023-10-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_app_url_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='url_main',
            field=models.URLField(default='/'),
        ),
    ]
