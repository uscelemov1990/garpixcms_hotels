from ..models.booking import Booking
from django.contrib import admin


@admin.register(Booking)
class BookingPageAdmin(admin.ModelAdmin):
    pass

# @admin.register(Booking)
# class BookingPageAdmin(admin.ModelAdmin):
#     list_display = ('arrival_date', 'date_of_departure', 'adults', 'children')
#     readonly_fields = ('id',)
