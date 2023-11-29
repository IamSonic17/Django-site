from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_home, name='reviews_home'),
    path('/<int:pk>', views.ReviewsDetailView.as_view(), name='reviews_detail')
]
