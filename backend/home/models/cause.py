from django.db import models


class Cause(models.Model):
    name = models.CharField(max_length=150, verbose_name='причина')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Причина"
        verbose_name_plural = "Причины"
        ordering = ("id",)
