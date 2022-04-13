from ..models.tagline import Tagline
from django.contrib import admin


@admin.register(Tagline)
class TaglinePageAdmin(admin.ModelAdmin):
    pass
