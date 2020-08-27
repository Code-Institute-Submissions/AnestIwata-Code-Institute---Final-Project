from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature


def index(request):
    bugs = Bug.objects.all()
    features = Feature.objects.all()
    context = {"bugs": len(bugs),
               "features": len(features)}
    return render(request, 'landing/index.html', context)
