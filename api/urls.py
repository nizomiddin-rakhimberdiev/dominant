from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, ServiceViewSet

app_name='api'

router = DefaultRouter()
router.register('services', ServiceViewSet, basename='service')
router.register('orders', OrderViewSet, basename='order')

urlpatterns = router.urls