from django.urls import path

from api.views import news, NewsDetailView, comments

urlpatterns = [
    path('news/<int:pk>/comments/', comments),
    path('news/<int:pk>/', NewsDetailView.as_view()),
    path('news/', news),

]