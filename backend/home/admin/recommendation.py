from ..models.recommendation import Recommendation
from django.contrib import admin


@admin.register(Recommendation)
class RecommendationPageAdmin(admin.ModelAdmin):
    pass
