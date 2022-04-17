from django.db import models
from garpix_page.models import BaseListPage


class HotelListPage(BaseListPage):
    paginate_by = 5
    # template = 'pages/hotel_list.html'

    class Meta:
        verbose_name = "HotelList"
        verbose_name_plural = "HotelLists"
        ordering = ('-created_at',)
