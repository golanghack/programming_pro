from django.urls import path
from students import views

urlpatterns = [
    path('register/', views.StudentsRegistrationView.as_view(), name='student_registration'),
]