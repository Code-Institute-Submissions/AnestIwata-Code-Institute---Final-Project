from django.urls import path, include
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'projects_main'

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='projects'),
    path('<int:pk>/', login_required(views.ProjectView.as_view()), name='project page'),
    path('<int:project_id>/comment/', views.add_comment, name='add comment'),
    path('<int:project_id>/vote/', views.vote, name='vote'),
    path('add_project/', views.create_project, name='add project'),
    path('<int:project_id>/delete_project/', views.delete_project, name='delete project'),
]
