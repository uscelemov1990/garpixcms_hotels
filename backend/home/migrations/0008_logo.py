# Generated by Django 3.1 on 2022-04-12 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_additionally'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='frontend/static/img')),
            ],
            options={
                'verbose_name': 'Лого',
            },
        ),
    ]
