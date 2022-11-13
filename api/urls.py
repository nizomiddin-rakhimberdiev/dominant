from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (OrderViewSet,
                    ServiceViewSet,
                    ReviewViewSet,
                    CategoryViewSet,
                    CategoryServiceViewSet,
                    NewsViewSet,
                    CandidateViewSet,
                    ConsultationViewSet
                    )

app_name = 'api'

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('services', ServiceViewSet, basename='service')
router.register('category-services', CategoryServiceViewSet, basename='category_service')
router.register('orders', OrderViewSet, basename='order')
router.register('reviews', ReviewViewSet, basename='review')
router.register('news', NewsViewSet, basename='news')
router.register('candidates', CandidateViewSet, basename='candidate')
router.register('consultations', ConsultationViewSet, basename='consultation')

urlpatterns = router.urls
