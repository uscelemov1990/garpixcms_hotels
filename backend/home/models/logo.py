from django.db import models


class Logo(models.Model):
    logo = models.ImageField()

    def __str__(self):
        return f'Лого'

    class Meta:
        verbose_name = "Лого"
        verbose_name_plural = "Лого"
