# Generated by Django 3.1 on 2022-04-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20220412_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='logo',
            field=models.FileField(upload_to=''),
        ),
    ]
