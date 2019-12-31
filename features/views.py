from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import generic
from .models import Feature
from .forms import CreateFeatureForm


class IndexView(generic.ListView):
    """
    Render a list of features.
    """
    template_name = 'features/index.html'
    context_object_name = 'features_list'

    def get_queryset(self):
        """Return all of the features"""
        return Feature.objects.all()


class FeatureView(generic.DetailView):
    """
    Render a single feature.
    """
    model = Feature
    template_name = 'features/feature.html'


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


def delete_feature(request, feature_id):
    """
    Delete a feature
    """
    try:
        Feature.objects.filter(pk=feature_id).delete()
        return redirect('features_main:features')
    except:
        return redirect('features_main:features')


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
