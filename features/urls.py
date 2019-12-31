from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='features'),
    path('<int:feature_id>/', views.feature, name='feature page'),
    path('<int:feature_id>/comment/', views.add_comment, name='add comment'),
    path('<int:feature_id>/vote/', views.vote, name='vote'),
]