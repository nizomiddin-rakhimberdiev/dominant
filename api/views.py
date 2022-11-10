from django.shortcuts import render
from rest_framework import viewsets

from .models import Service, Order
from .serializers import ServiceSerializer, OrderSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().order_by('created_at')
    lookup_field = 'id'


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('created_at')
    lookup_field = 'id'
