from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .models import Project
from .forms import CreateProjectForm
from accounts.models import Profile


class IndexView(generic.ListView):
    """
    Render a list of projects.
    """
    template_name = 'projects/index.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        """Return all of the projects"""
        return Project.objects.all()


class ProjectView(generic.DetailView):
    """
    Render a single project.
    """
    model = Project
    template_name = 'projects/project.html'


@login_required
def create_project(request):
    """
    Create a project.
    """
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            retrieved_project = form.save(commit=False)
            author = Profile.objects.get(user=request.user)
            retrieved_project.author = author
            retrieved_project.save()
            return redirect('projects_main:project page', retrieved_project.pk)
    else:
        form = CreateProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})


@login_required
def delete_project(request, project_id):
    """
    Delete a project
    """
    try:
        Project.objects.filter(pk=project_id).delete()
        return redirect('projects_main:projects')
    except:
        return redirect('projects_main:projects')


@login_required
def add_comment(request, project_id):
    """
    Add a comment to a project.
    """
    return HttpResponse("This is a panel to add a comment")


@login_required
def vote(request, project_id):
    """
    Allow user to vote for project.
    """
    retrieved_project = Project.objects.get(pk=project_id)
    retrieved_project.upvotes += 1
    retrieved_project.save()
    return redirect('projects_main:project page', project_id)
