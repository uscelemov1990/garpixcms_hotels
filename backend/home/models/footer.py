from django.db import models


class Footer(models.Model):
    hashtag = models.CharField(max_length=20, verbose_name='хештег', default='#VISITSEDONA')
    phone = models.CharField(max_length=20, blank=True, verbose_name='телефон')
    twitter = models.CharField(max_length=60, blank=True, verbose_name='twitter')
    facebook = models.CharField(max_length=60, blank=True, verbose_name='facebook')
    youtube = models.CharField(max_length=60, blank=True, verbose_name='youtube')

    def __str__(self):
        return self.hashtag

    class Meta:
        verbose_name = "Подвал"
        verbose_name_plural = "Подвал"
        ordering = ("id",)
