from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user


def create_user_account(username, email, password, first_name="",
                        last_name="", phone_number="", address="", **extra_fields):
    user = get_user_model().objects.create_user(
        username=username, email=email, password=password, first_name=first_name,
        last_name=last_name, phone_number=phone_number, address=address, **extra_fields)
    return user
