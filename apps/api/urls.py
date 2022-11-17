from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()
router.register('orders', views.OrderViewSet, basename='order')
router.register('reviews', views.ReviewViewSet, basename='review')
router.register('candidates', views.CandidateViewSet, basename='candidate')
router.register('consultations', views.ConsultationViewSet, basename='consultation')

urlpatterns = router.urls

urlpatterns += [
    path('services/', views.ServiceListAPIView.as_view(), name='service'),
    path('categories/', views.CategoryListAPIView.as_view(), name='categories'),
    path('category-services/', views.CategoryServiceListAPIView.as_view(), name='category-service'),
    path('news/', views.NewsListAPIView.as_view(), name='news'),
    path('news/<int:pk>/', views.NewsDetailAPIView.as_view(), name='news-detail'),
    path('category-services/<int:pk>/', views.CategoryServiceDetailAPIView.as_view(), name='category-service-detail'),
    path('services/<int:pk>/', views.ServiceDetailAPIView.as_view(), name='service-detail'),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category-detail'),
]