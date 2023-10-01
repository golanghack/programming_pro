from django.urls import path
from users.views import UsersRegistrationView

urlpatterns = [
    path('register/', UsersRegistrationView.as_view(), name='registration'),
]