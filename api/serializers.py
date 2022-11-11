from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import CustomUser
from .models import Service, Order, Review


class ServiceSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Service
        fields = ('id',
                  'name',
                  'no_action_price',
                  'action_price',
                  'created_at'
                  )


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id",
                  "first_name",
                  "last_name",
                  "username",
                  "email",
                  'phone_number',
                  'address'
                  )


class OrderSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)

    user_id = serializers.IntegerField(write_only=True)
    service_id = serializers.IntegerField(write_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        fields = ('id',
                  'user',
                  'user_id',
                  'phone',
                  'service',
                  'service_id',
                  'number_of_loader',
                  'number_of_hour',
                  'floor', 'elevator',
                  'need_a_car',
                  'created_at'
                  )


class ReviewSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    user_id = serializers.IntegerField(write_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Review
        fields = ('id',
                  'user',
                  'user_id',
                  'comment',
                  'star',
                  'created_at'
                  )


# Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username',
                  'password',
                  'password2',
                  'email',
                  'phone_number',
                  'first_name',
                  'last_name'
                  )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
