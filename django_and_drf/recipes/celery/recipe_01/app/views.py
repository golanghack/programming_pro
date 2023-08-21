from rest_framework.generics import CreateAPIView
from app.models import Order, Shipment
from app.serializers import OrderSerializer, ShipmentSerializer

class CreateOrderView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CreateShipmentView(CreateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()