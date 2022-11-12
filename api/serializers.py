from rest_framework import serializers

from users.models import CustomUser
from .models import Service, Order, Review, News, Category, CategoryService, Candidate, Consultation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'price', 'action_price')

class CategoryServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    service = ServiceSerializer(read_only=True)
    service_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CategoryService
        fields = ('id', 'service', 'service_id', 'category', 'category_id')

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "username", 'phone_number', 'profile_pic', 'address')

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

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'subTitle', 'photo', 'time_update', 'views', 'content')

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        read_only_fields = ('created_at', 'updated_at')
        # phone field-ni uchirib tashlab, phone yuq forma to'ldirib post qilsa bazaga saqlab quyyabdi.
        # vaholangki phone required=True bo'lishi(blank = False) kerak.
        fields = ('id', 'fullname', 'resume', 'service', 'phone', 'created_at', 'updated_at')

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        read_only_fields = ('created_at')
        fields = ('id', 'fullname', 'phone', 'status', 'created_at')
