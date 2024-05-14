from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404

from studies.models import Activity


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def stats(request):
    # Represent information about all studies
    all_activities = get_list_or_404(Activity)
    context = {'studies_objs': all_activities,
               'number_of_studies': all_activities.count(),
               'consonants': all_activities.filter(type="CNS").count(),
               'courses': all_activities.filter(type="CRS").count(),
               'books': all_activities.filter(type="BOK").count(),
               'title': "Studies statistic page"}

    return render(request, 'studies/stats.html', context=context)
