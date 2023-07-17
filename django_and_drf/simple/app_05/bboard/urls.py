from django.urls import path 
from bboard.views import index

urlpatterns = [
    path('', index),
]