# Generated by Django 3.1 on 2022-04-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220412_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='logo',
            field=models.FileField(upload_to='', verbose_name='/home/alexey/.local/share/virtualenvs/garpix1-yAXXW8T9/lib/python3.8/site-packages/static/img'),
        ),
    ]