from django.urls import path

from api.views import news

urlpatterns = [
    path('news/', news),
]