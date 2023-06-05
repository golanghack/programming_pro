from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path('lists/new$', views.new_list, name='new_list'),
    re_path('lists/(.+)/$', views.view_list, name='view_list'),
]