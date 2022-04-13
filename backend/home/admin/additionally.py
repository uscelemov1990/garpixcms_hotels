from ..models.additionally import Additionally
from django.contrib import admin


@admin.register(Additionally)
class AdditionallyPageAdmin(admin.ModelAdmin):
    pass
