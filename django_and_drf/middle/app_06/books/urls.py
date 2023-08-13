from django.urls import path
from books.views import Books

urlpatterns = [
    path('', Books.as_view(), name='home'),
]