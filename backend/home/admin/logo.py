from ..models.logo import Logo
from django.contrib import admin


@admin.register(Logo)
class LogoPageAdmin(admin.ModelAdmin):
    pass
