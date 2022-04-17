from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    model_hostel = models.CharField(max_length=150, verbose_name='модель')
    price_min = models.IntegerField(verbose_name='цена минимальная')
    price_max = models.IntegerField(verbose_name='цена максимальная')
    rating = models.FloatField(verbose_name='рейтинг')
    image = models.ImageField(upload_to='hotel', verbose_name='фото')
    stars = models.IntegerField(default=1, verbose_name='количество звезд')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"
        ordering = ("id",)
