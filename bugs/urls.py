from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'bugs_main'

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='bugs'),
    path('<int:pk>/', login_required(views.BugView.as_view()), name='bug page'),
    path('<int:bug_id>/vote/', views.vote, name='vote'),
    path('add_bug/', views.create_bug, name='add bug'),
    path('<int:bug_id>/delete_bug/', views.delete_bug, name='delete bug'),
]
