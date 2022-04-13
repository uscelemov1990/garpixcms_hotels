from django.db import models
from garpix_menu.mixins import LinkMixin

from .cause import Cause


class Recommendation(LinkMixin):
    cause = models.OneToOneField(Cause, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='рекомендация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"
        ordering = ("id",)
