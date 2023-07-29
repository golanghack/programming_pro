from django.urls import path
from main.views import (index, 
                        other_page, 
                        AppLoginView,
                        profile)

app_name = 'main'
urlpatterns = [
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', AppLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]