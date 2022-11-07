from rest_framework import serializers

from .models import Service, Order


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'no_action_price', 'action_price', 'created_at')


class OrderSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)

    service_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = ('id', 'phone', 'service', 'service_id', 'order_status', 'offera', 'created_at')
