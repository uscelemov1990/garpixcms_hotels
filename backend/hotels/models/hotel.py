from django.db import models


class Hotel(models.Model):
    MODEL_HOSTEL = (
        ('МОТЕЛЬ', 'МОТЕЛЬ'),
        ('ГОСТИНИЦА', 'ГОСТИНИЦА'),
        ('АПАРТАМЕНТЫ', 'АПАРТАМЕНТЫ'),
    )
    name = models.CharField(max_length=150, verbose_name='название')
    model_hostel = models.CharField(max_length=150, choices=MODEL_HOSTEL, verbose_name='модель')
    price_min = models.IntegerField(verbose_name='цена минимальная')
    price_max = models.IntegerField(verbose_name='цена максимальная', blank=True)
    rating = models.FloatField(verbose_name='рейтинг')
    image = models.ImageField(upload_to='hotel', verbose_name='фото')
    stars = models.IntegerField(default=1, verbose_name='количество звезд')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"
        ordering = ("price_min",)
