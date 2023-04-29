from django.urls import path 
from .views import ContactBuilder, correct

urlpatterns = [
    path('contact/', ContactBuilder.as_view(), name='contact'), 
    path('correct/', correct, name='correct'),
]