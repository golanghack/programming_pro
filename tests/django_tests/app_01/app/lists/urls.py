from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/unic_list/', views.view_list, name='view_list'),
]