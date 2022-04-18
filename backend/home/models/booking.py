from django.db import models


class Booking(models.Model):
    arrival_date = models.DateField(verbose_name='дата заезда')
    date_of_departure = models.DateField(verbose_name='дата выезда')
    adults = models.PositiveIntegerField(verbose_name='взрослые')
    kids = models.PositiveIntegerField(verbose_name='дети', blank=True)

    def __str__(self):
        return f'{self.arrival_date} - {self.date_of_departure}. Взрослых - {self.adults}, детей - {self.kids}'

    class Meta:
        verbose_name = "Бронировние"
        verbose_name_plural = "Бронировния"
        ordering = ("id",)
