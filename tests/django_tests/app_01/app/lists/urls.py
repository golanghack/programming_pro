from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/new', views.new_list, name='new_list'),
    path('lists/<int:id>/', views.view_list, name='view_list'),
]