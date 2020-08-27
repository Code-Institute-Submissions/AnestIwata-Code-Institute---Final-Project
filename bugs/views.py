from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import generic
from .models import Bug
from .forms import CreateBugForm
from accounts.models import Profile
from projects.models import Project


class IndexView(generic.ListView):
    """
    Render a list of bugs.
    """
    template_name = 'bugs/index.html'
    context_object_name = 'bugs_list'

    def get_queryset(self):
        """Return all of the bugs"""
        return Bug.objects.all()


class BugView(generic.DetailView):
    """
    Render a single bug.
    """
    model = Bug
    template_name = 'bugs/bug.html'


@login_required
def create_bug(request):
    """
    Create a bug.
    """
    if request.method == "POST":
        form = CreateBugForm(request.POST)
        if form.is_valid():
            retrieved_bug = form.save(commit=False)
            author = Profile.objects.get(user=request.user)
            retrieved_bug.author = author
            retrieved_bug.save()
            return redirect('bugs_main:bug page', retrieved_bug.pk)
    else:
        form = CreateBugForm()
    return render(request, 'bugs/add_bug.html', {'form': form})


@login_required
def delete_bug(request, bug_id):
    """
    Delete a bug
    """
    try:
        Bug.objects.filter(pk=bug_id).delete()
        return redirect('bugs_main:bugs')
    except:
        return redirect('bugs_main:bugs')


@login_required
def vote(request, bug_id):
    """
    Allow user to vote for bug.
    """
    retrieved_bug = Bug.objects.get(pk=bug_id)
    retrieved_bug.upvotes += 1
    retrieved_bug.save()
    return redirect('bugs_main:bug page', bug_id)
