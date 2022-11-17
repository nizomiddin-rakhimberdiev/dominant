from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Service, Order, Review, Category, CategoryService, Consultation, Candidate, News
from .serializers import ServiceSerializer, OrderSerializer, ReviewSerializer, CategorySerializer, \
    CategoryServiceSerializer, ConsultationSerializer, CandidateSerializer, NewsSerializer


class CategoryListAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(data=serializer.data)


class ServiceListAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        services = Service.objects.all().order_by('created_at')
        serializer = ServiceSerializer(services, many=True)
        return Response(data=serializer.data)

class CategoryServiceListAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        category_service = CategoryService.objects.all()
        serializer = CategoryServiceSerializer(category_service, many=True)
        return Response(data=serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('created_at')
    lookup_field = 'id'


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by('created_at')
    lookup_field = 'id'


class NewsListAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        news = News.objects.all().order_by('time_update')
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all().order_by('created_at')
    lookup_field = 'id'

class ConsultationListAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        consultation = Consultation.objects.all()
        serializer = ConsultationSerializer(consultation, many=True)
        return Response(data=serializer.data)
