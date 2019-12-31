from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Feature
from .forms import CreateFeatureForm


def index(request):
    """
    Render a list of features.
    """
    # features = Feature.objects.all()
    features = get_list_or_404(Feature)
    context = {
        'features_list': features,
    }
    return render(request, 'features/index.html', context)


def feature(request, feature_id):
    """
    Render a single feature.
    """
    retrieved_feature = get_object_or_404(Feature, pk=feature_id)

    return render(request, 'features/feature.html', {'feature': retrieved_feature})


def create_feature(request):
    """
    Create a feature.
    """
    if request.method == "POST":
        form = CreateFeatureForm(request.POST)
        if form.is_valid():
            retrieved_feature = form.save()
            return redirect('features_main:feature page', retrieved_feature.pk)
    else:
        form = CreateFeatureForm()
    return render(request, 'features/add_feature.html', {'form': form})


def add_comment(request, feature_id):
    """
    Add a comment to a feature.
    """
    return HttpResponse("This is a panel to add a comment")


def vote(request, feature_id):
    """
    Allow user to vote for feature.
    """
    retrieved_feature = Feature.objects.get(pk=feature_id)
    retrieved_feature.upvotes += 1
    retrieved_feature.save()
    return redirect('features_main:feature page', feature_id)
