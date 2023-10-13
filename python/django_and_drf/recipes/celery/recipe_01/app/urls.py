from django.urls import path
from app.views import CreateOrderView, CreateShipmentView

urlpatterns = [
    path('orders', CreateOrderView.as_view()),
    path('shipments', CreateShipmentView.as_view()),
]