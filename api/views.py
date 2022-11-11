from django.shortcuts import render
from rest_framework import viewsets

from .models import Service, Order, Review
from .serializers import ServiceSerializer, OrderSerializer, ReviewSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().order_by('created_at')
    lookup_field = 'id'


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('created_at')
    lookup_field = 'id'


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by('created_at')
    lookup_field = 'id'
