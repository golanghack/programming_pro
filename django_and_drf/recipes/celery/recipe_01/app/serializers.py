from rest_framework import serializers
from app.models import Order, Shipment

class OrderSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Order
        fields = ['id', 'name', 'quantity', 'weight', 'price', 'created_at']

class ShipmentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.IntegerField()

    class Meta:
        model = Shipment
        fields = [
            'id_reference',
            'order', 
            'order_id', 
            'address', 
            'owner_name',
            'owner_email',
            'shipment_date',
            'status',
        ] 

    def create(self, validated_data):
        try:
            order = Order.objects.get(id=validated_data['order_id'])
            shipment = Shipment.objects.create(order=order, **validated_data)

            return shipment
        except Order.DoesNotExist:
            return serializers.ValidationError('This order didi not find')