# Generated by Django 3.1 on 2022-04-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_auto_20220413_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='stars',
            field=models.ImageField(blank=True, upload_to='', verbose_name='количество звезд'),
        ),
    ]
