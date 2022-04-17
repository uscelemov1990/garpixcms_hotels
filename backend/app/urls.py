from garpixcms.urls import *  # noqa


urlpatterns = [
    path('home/', include('home.urls')),
    path('hotels/', include('hotels.urls')),
              ] + urlpatterns  # noqa
