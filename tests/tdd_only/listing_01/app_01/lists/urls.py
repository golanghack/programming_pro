from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lists/one/', views.view_list, name='view_list'),
]