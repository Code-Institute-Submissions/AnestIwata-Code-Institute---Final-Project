from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello this is features page.")

def feature(request, feature_id):
    return HttpResponse("This is a single feature")

def add_comment(request, feature_id):
    return HttpResponse("This is a panel to add a comment")

def vote(request, feature_id):
    return HttpResponse("This is a function to vote on a feature")
