from django.core.paginator import Paginator
from django.shortcuts import render

from ..models import Hotel
from home.models.logo import Logo
from home.models.footer import Footer


def hotels(request):
    hotel = Hotel.objects.all()
    paginator = Paginator(hotel, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    logo = Logo.objects.first()
    footer = Footer.objects.first()

    context = {
        'hotel': hotel,
        'page_obj': page_obj,
        'logo': logo,
        'footer': footer
    }
    return render(request, 'pages/hotels.html', context)
