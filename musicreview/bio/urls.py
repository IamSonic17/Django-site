from django.urls import path
from . import views

urlpatterns = [
    path('', views.bio_home, name='bio_home'),
    path('/<int:pk>', views.BioDetailView.as_view(), name='bio_detail')
]
