from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_home, name='book_home'),
    path('/add/', views.add_message_view, name='add_message'),
    path('/register/', views.register_new_user, name='new_user')
]