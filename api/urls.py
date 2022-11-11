from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, ServiceViewSet, ReviewViewSet

app_name = 'api'

router = DefaultRouter()
router.register('services', ServiceViewSet, basename='service')
router.register('orders', OrderViewSet, basename='order')
router.register('reviews', ReviewViewSet, basename='review')
urlpatterns = router.urls
