from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
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

class CategoryListDetail(APIView):
    permission_classes = (AllowAny,)
    def get(self,request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class ServiceListAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        services = Service.objects.all().order_by('created_at')
        serializer = ServiceSerializer(services, many=True)
        return Response(data=serializer.data)

class ServiceListDetail(APIView):
    permission_classes = (AllowAny,)
    def get(self,request, pk):
        service = get_object_or_404(Service, pk=pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)
    def delete(self,request, pk):
        service = get_object_or_404(Service, pk=pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryServiceListAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        category_service = CategoryService.objects.all()
        serializer = CategoryServiceSerializer(category_service, many=True)
        return Response(data=serializer.data)

class CategoryServiceListDetail(APIView):
    permission_classes = (AllowAny,)
    def get(self,request, pk):
        category_service = get_object_or_404(CategoryService, pk=pk)
        serializer = CategoryServiceSerializer(category_service)
        return Response(serializer.data)




class NewsListAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        news = News.objects.all().order_by('time_update')
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

class NewsListDetail(APIView):
    permission_classes = (AllowAny,)
    def get(self,request, pk):
        news = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)
    def delete(self,request, pk):
        news = get_object_or_404(News, pk=pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConsultationListAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        consultation = Consultation.objects.all()
        serializer = ConsultationSerializer(consultation, many=True)
        return Response(data=serializer.data)

class ConsultationListDetail(APIView):
    permission_classes = (AllowAny,)
    def get(self,request, pk):
        сonsultations = get_object_or_404(Consultation, pk=pk)
        serializer = ConsultationSerializer(сonsultations)
        return Response(serializer.data)
    def delete(self,request, pk):
        сonsultations = get_object_or_404(Consultation, pk=pk)
        сonsultations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all().order_by('created_at')
    lookup_field = 'id'

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('created_at')
    lookup_field = 'id'


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by('created_at')
    lookup_field = 'id'
