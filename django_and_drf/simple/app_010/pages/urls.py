from django.urls import path
from pages.views import HomeView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]