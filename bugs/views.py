from django.shortcuts import render
from .models import Bug


def index(request):
    bugs = Bug.objects.all()
    context = {
        'bugs_list': bugs,
    }
    return render(request, 'bugs/index.html', context)
