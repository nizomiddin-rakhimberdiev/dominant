from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.users.models import CustomUser
from .models import Service, Order, Review, Category, News, Candidate, CategoryService, Consultation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'name',
                  'created_at'
                  )
        read_only_fields = ('created_at',)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id',
                  'name',
                  'price',
                  'action_price',
                  'created_at'
                  )
        read_only_fields = ('created_at',)


class CategoryServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    service = ServiceSerializer(read_only=True)
    service_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CategoryService
        fields = ('id',
                  'service',
                  'service_id',
                  'category',
                  'category_id'
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

    class Meta:
        model = Order
        read_only_fields = ('created_at',)
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

    class Meta:
        model = Review
        read_only_fields = ('created_at',)
        fields = ('id',
                  'user',
                  'user_id',
                  'comment',
                  'star',
                  'created_at'
                  )



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id',
                  'title',
                  'subTitle',
                  'photo',
                  'time_update',
                  'views',
                  'content',
                  'created_at'
                  )
        read_only_fields = ('created_at',)


class CandidateSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)

    service_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Candidate
        read_only_fields = ('created_at',)
        # phone field-ni uchirib tashlab, phone yuq forma to'ldirib post qilsa bazaga saqlab quyyabdi.
        # vaholangki phone required=True bo'lishi(blank = False) kerak.
        fields = ('id',
                  'fullname',
                  'resume',
                  'service',
                  'service_id',
                  'phone',
                  'created_at',
                  )


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        read_only_fields = ('created_at', 'status')
        fields = ('id',
                  'fullname',
                  'phone',
                  'status',
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
