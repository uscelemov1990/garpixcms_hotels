from django.shortcuts import render

from ..models import Tagline, Footer
from ..models.logo import Logo
from ..models.recommendation import Recommendation
from ..models.additionally import Additionally


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

    context = {
        'recommendation_1': recommendation_1,
        'recommendation_2': recommendation_2,
        'recommendation_3_5': recommendation_3_5,
        'additionally': additionally,
        'logo': logo,
        'tagline': tagline,
        'footer': footer,
    }
    return render(request, 'pages/home.html', context)
