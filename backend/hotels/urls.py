from django.urls import path

# from .views.hotel import Hotels
from .views.hotel import hotels

urlpatterns = [
    # path('', Hotels, name='hotels'),
    path('', hotels, name='hotels'),
]
