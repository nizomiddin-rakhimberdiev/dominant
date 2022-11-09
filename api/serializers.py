from rest_framework import serializers

from users.models import CustomUser
from .models import Service, Order, Review


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'no_action_price', 'action_price', 'created_at')

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "username", 'phone_number', 'profile_pic', 'address']

class OrderSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)

    service_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = ('id', 'phone', 'service', 'service_id', 'order_status', 'offera', 'created_at')

class ReviewSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Review
        fields = ('id', 'user', 'user_id', 'comment', 'star', 'created_at')