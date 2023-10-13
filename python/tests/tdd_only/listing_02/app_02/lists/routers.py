from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('new$', views.new_list, name='new_list'),
    re_path('(\d+)/$', views.view_list, name='view_list'),
]