from ..models.cause import Cause
from django.contrib import admin


@admin.register(Cause)
class CausePageAdmin(admin.ModelAdmin):
    pass
