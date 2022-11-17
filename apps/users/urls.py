from rest_framework import routers

from apps.users.views import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('', AuthViewSet, basename='auth')

urlpatterns = router.urls
