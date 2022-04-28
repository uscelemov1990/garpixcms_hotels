from django.core.paginator import Paginator
from django.shortcuts import render

from ..forms.hotel import HotelFilterForm
from ..models import Hotel
from home.models.logo import Logo
from home.models.footer import Footer


def hotels(request):
    hotel = Hotel.objects.order_by('rating')

    form = HotelFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['price_min']:
            hotel = hotel.filter(price_min__gte=form.cleaned_data['price_min'])

        if form.cleaned_data['price_max']:
            hotel = hotel.filter(price_min__lte=form.cleaned_data['price_max'])

        if form.cleaned_data['ordering']:
            hotel = hotel.order_by(form.cleaned_data['ordering'])

        if form.cleaned_data['ordering_price']:
            hotel = hotel.order_by(form.cleaned_data['ordering_price'])

        if form.cleaned_data['ordering_model']:
            hotel = hotel.order_by(form.cleaned_data['ordering_model'])

        if form.cleaned_data['ordering_rating']:
            hotel = hotel.order_by(form.cleaned_data['ordering_rating'])

    paginator = Paginator(hotel, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    logo = Logo.objects.first()
    footer = Footer.objects.first()

    context = {
        'hotel': hotel,
        'page_obj': page_obj,
        'logo': logo,
        'footer': footer,
        'form': form,
    }
    return render(request, 'pages/hotels.html', context)
