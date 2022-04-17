from ..models.hotel import Hotel
from django.contrib import admin


@admin.register(Hotel)
class HotelPageAdmin(admin.ModelAdmin):
    pass
