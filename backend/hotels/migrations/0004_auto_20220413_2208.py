# Generated by Django 3.1 on 2022-04-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotel_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='stars',
            field=models.IntegerField(blank=True, verbose_name='количество звезд'),
        ),
    ]