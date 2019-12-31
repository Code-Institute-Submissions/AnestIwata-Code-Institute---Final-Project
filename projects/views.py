from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Project


def index(request):
    projects = get_list_or_404(Project)
    context = {
        'projects_list': projects,
    }
    return render(request, 'projects/index.html', context)