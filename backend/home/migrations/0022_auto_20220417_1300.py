# Generated by Django 3.1 on 2022-04-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20220417_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.TextField(verbose_name='дата заезда'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_of_departure',
            field=models.TextField(verbose_name='дата выезда'),
        ),
    ]