from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=50, verbose_name='бронировние', default='бронировние')
    arrival_date = models.DateField(verbose_name='дата заезда')
    date_of_departure = models.DateField(verbose_name='дата выезда')
    adults = models.IntegerField(verbose_name='взрослые')
    children = models.IntegerField(verbose_name='дети')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бронировние"
        verbose_name_plural = "Бронировния"
        ordering = ("id",)
