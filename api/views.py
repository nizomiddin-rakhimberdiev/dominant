from django.shortcuts import render
from rest_framework import viewsets

from .models import Service, Order, Review, Category, CategoryService, Consultation, Candidate, News
from .serializers import ServiceSerializer, OrderSerializer, ReviewSerializer, CategorySerializer, \
    CategoryServiceSerializer, ConsultationSerializer, CandidateSerializer, NewsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('id')
    lookup_field = 'id'


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().order_by('created_at')
    lookup_field = 'id'


class CategoryServiceViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryServiceSerializer
    queryset = CategoryService.objects.all().order_by('created_at')
    lookup_field = 'id'


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('created_at')
    lookup_field = 'id'


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by('created_at')
    lookup_field = 'id'


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all().order_by('time_update')
    lookup_field = 'id'


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all().order_by('created_at')
    lookup_field = 'id'


class ConsultationViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultationSerializer
    queryset = Consultation.objects.all().order_by('created_at')
    lookup_field = 'id'
