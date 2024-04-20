from django.http import HttpResponse
from django.shortcuts import render

from studies.models import Activity


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def stats(request):
    # Represent information about all studies
    context = {'studies': Activity.objects.all()}

    return render(request, 'studies/stats.html', context=context)
