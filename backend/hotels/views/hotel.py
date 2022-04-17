from django.core.paginator import Paginator
from django.shortcuts import render

from ..models import Hotel


def hotels(request):
    hotel = Hotel.objects.all()
    paginator = Paginator(hotel, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'hotel': hotel,
        'page_obj': page_obj,
    }
    return render(request, 'pages/hotels.html', context)
