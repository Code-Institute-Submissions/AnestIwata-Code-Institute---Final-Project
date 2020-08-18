from django.urls import path, include
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'features_main'
urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='features'),
    path('<int:pk>/', login_required(views.FeatureView.as_view()), name='feature page'),
    path('<int:feature_id>/comment/', views.add_comment, name='add comment'),
    path('<int:feature_id>/vote/', views.vote, name='vote'),
    path('add_feature/', views.create_feature, name='add feature'),
    path('<int:feature_id>/delete_feature/', views.delete_feature, name='delete feature'),
]
