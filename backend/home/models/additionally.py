from django.db import models


class Additionally(models.Model):
    name = models.CharField(max_length=150, verbose_name='причина')
    description = models.CharField(max_length=150, verbose_name='рекомендация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Причина дополнительно"
        verbose_name_plural = "Причины дополнительно"
        ordering = ("id",)
