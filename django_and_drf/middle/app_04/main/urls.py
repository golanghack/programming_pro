from django.urls import path
from main.views import index, other_page, AppLoginView

app_name = 'main'
urlpatterns = [
    path('accounts/login/', AppLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]