from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Feature


def index(request):
    # features = Feature.objects.all()
    features = get_list_or_404(Feature)
    context = {
        'features_list': features,
    }
    return render(request, 'features/index.html', context)


def feature(request, feature_id):
    retrieved_feature = get_object_or_404(Feature, pk=feature_id)

    return render(request, 'features/index.html', {'feature': retrieved_feature})


def add_comment(request, feature_id):
    return HttpResponse("This is a panel to add a comment")


def vote(request, feature_id):
    return HttpResponse("This is a function to vote on a feature")
