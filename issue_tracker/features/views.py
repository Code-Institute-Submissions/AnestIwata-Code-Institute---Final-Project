from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Feature


def index(request):
    features = Feature.objects.all()
    context = {
        'features_list': features,
    }
    return render(request, 'features/index.html', context)


def feature(request, feature_id):
    try:
        retrieved_feature = Feature.objects.get(pk=feature_id)
    except:
        raise Http404('Feature does not exist')
    return render(request, 'features/index.html', {'feature': retrieved_feature})


def add_comment(request, feature_id):
    return HttpResponse("This is a panel to add a comment")


def vote(request, feature_id):
    return HttpResponse("This is a function to vote on a feature")
