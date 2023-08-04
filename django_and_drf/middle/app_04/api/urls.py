from django.urls import path

from api.views import news, NewsDetailView

urlpatterns = [
    path('news/<int:pk>/', NewsDetailView.as_view()),
    path('news/', news),

]