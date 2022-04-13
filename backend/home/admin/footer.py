from ..models.footer import Footer
from django.contrib import admin


@admin.register(Footer)
class FooterPageAdmin(admin.ModelAdmin):
    pass
