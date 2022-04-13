from django.db import models


class Logo(models.Model):
    logo = models.ImageField()

    class Meta:
        verbose_name = "Лого"
        verbose_name_plural = "Лого"
