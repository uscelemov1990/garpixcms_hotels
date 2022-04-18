from django.shortcuts import render, redirect

from ..models import Tagline, Footer
from ..models.logo import Logo
from ..models.recommendation import Recommendation
from ..models.additionally import Additionally
from ..forms.booking import BookingForm
from garpix_notify.models import Notify
from django.conf import settings


def home(request):
    recommendation = Recommendation.objects.all()
    recommendation_1 = [recommendation[0], 1]
    recommendation_2 = [recommendation[1], 2]
    recommendation_3_5 = [
        [recommendation[2], 3],
        [recommendation[3], 4],
        [recommendation[4], 5],
        ]

    additionally = Additionally.objects.all()[:3]
    tagline = Tagline.objects.first()

    logo = Logo.objects.first()
    footer = Footer.objects.first()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            Notify.send(settings.FEEDBACK_EVENT, {
                'booking': booking,
            }, email='ustselemov90@yandex.ru')

    else:
        form = BookingForm()

    context = {
        'recommendation_1': recommendation_1,
        'recommendation_2': recommendation_2,
        'recommendation_3_5': recommendation_3_5,
        'additionally': additionally,
        'logo': logo,
        'tagline': tagline,
        'footer': footer,
        'form': form,
    }

    return render(request, 'pages/home.html', context)
