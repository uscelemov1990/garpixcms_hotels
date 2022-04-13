# Generated by Django 3.1 on 2022-04-10 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_page', '0001_initial'),
        ('home', '0004_recommendation'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='hash',
            field=models.CharField(blank=True, default='', help_text='Если хотите дать ссылку на конкретный элемент страницы. Например - #example', max_length=256, verbose_name='Якорь'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='home_page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='carousel_items', to='home.homepage', verbose_name='Страница (привязка)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recommendation',
            name='page',
            field=models.ForeignKey(blank=True, help_text='Если этот пункт не выбран, то будет использовано следующее поле "Внешний URL"', null=True, on_delete=django.db.models.deletion.CASCADE, to='garpix_page.basepage', verbose_name='Страница, на которую ведет пункт меню'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Внешний URL'),
        ),
    ]