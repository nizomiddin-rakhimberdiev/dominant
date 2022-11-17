from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Service, Order, Review, Category, CategoryService, Consultation, Candidate, News
from .serializers import ServiceSerializer, OrderSerializer, ReviewSerializer, CategorySerializer, \
    CategoryServiceSerializer, ConsultationSerializer, CandidateSerializer, NewsSerializer


class CategoryListAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)


class CategoryDetailAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class ServiceListAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        services = Service.objects.all().order_by('created_at')
        serializer = ServiceSerializer(services, many=True)
        return Response(data=serializer.data)


class ServiceDetailAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        service = get_object_or_404(Service, id=id)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)


class CategoryServiceListAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        category_service = CategoryService.objects.all()
        serializer = CategoryServiceSerializer(category_service, many=True)
        return Response(data=serializer.data)


class CategoryServiceDetailAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        category_service = get_object_or_404(CategoryService, id=id)
        serializer = CategoryServiceSerializer(category_service)
        return Response(serializer.data)


class NewsListAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        news = News.objects.all().order_by('time_update')
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class NewsDetailAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('created_at')
    lookup_field = 'id'


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by('created_at')
    lookup_field = 'id'


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all().order_by('created_at')
    lookup_field = 'id'


class ConsultationViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultationSerializer
    queryset = Consultation.objects.all().order_by('created_at')
    lookup_field = 'id'
