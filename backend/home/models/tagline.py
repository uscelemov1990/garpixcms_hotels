from django.db import models


class Tagline(models.Model):
    tagline = models.CharField(max_length=150, verbose_name='слоган')

    def __str__(self):
        return self.tagline

    class Meta:
        verbose_name = "Слоган"
        verbose_name_plural = "Слоганы"
        ordering = ("id",)
