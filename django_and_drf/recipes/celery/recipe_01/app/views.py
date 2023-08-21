from rest_framework.generics import CreateAPIView
from app.models import Order, Shipment
from app.serializers import OrderSerializer, ShipmentSerializer

class CreateOrder(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CreateShipment(CreateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()