# libs
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
# my 
from app.models import Order, Shipment
from app.serializers import OrderSerializer, ShipmentSerializer
from app.tasks import send_shipment_email

class CreateOrderView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CreateShipmentView(CreateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        owner_name = serializer.data['owner_name']
        order_name = serializer.data['order']['name']
        owner_email = serializer.data['owner_email']
        send_shipment_email.delay(owner_name, order_name, owner_email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)