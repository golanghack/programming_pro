from django.urls import path
from api.views import BookApiView

urlpatterns = [
    path('', BookApiView.as_view()),
]