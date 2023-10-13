from django.urls import path
from .views import SignupView


urlpatterns = [
    path(r'register', SignupView.as_view()),
]