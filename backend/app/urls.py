from garpixcms.urls import *  # noqa


urlpatterns = [
    path('home/', include('home.urls')),
              ] + urlpatterns  # noqa
