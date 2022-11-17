from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (OrderViewSet,
                    ServiceListAPI,
                    ReviewViewSet,
                    CategoryListAPI,
                    CategoryServiceListAPI,
                    NewsListAPI,
                    CandidateViewSet,
                    ConsultationListAPI, NewsListDetail, CategoryServiceListDetail, ConsultationListDetail,
                    ServiceListDetail, CategoryListDetail
                    )

app_name = 'api'

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='order')
router.register('reviews', ReviewViewSet, basename='review')
router.register('candidates', CandidateViewSet, basename='candidate')
# router.register('categories', CategoryListAPI, basename='category')
# router.register('services', ServiceListAPI.as_view(), basename='service')
# router.register('category-services', CategoryServiceViewSet, basename='category_service')
# router.register('news', NewsViewSet, basename='news')
# router.register('consultations', ConsultationListAPI, basename='consultation')

urlpatterns = router.urls

urlpatterns += [
    path('services/', ServiceListAPI.as_view(), name='service'),
    path('category/', CategoryListAPI.as_view(), name='category'),
    path('consultation/', ConsultationListAPI.as_view(), name='consultation'),
    path('category-service/', CategoryServiceListAPI.as_view(), name='category-service'),
    path('news/', NewsListAPI.as_view(), name='news'),
    path('news/<int:pk>/', NewsListDetail.as_view(), name='news-detail'),
    path('category-service/<int:pk>/', CategoryServiceListDetail.as_view(), name='category-service-detail'),
    path('consultation/<int:pk>/', ConsultationListDetail.as_view(), name='consultation-detail'),
    path('services/<int:pk>/', ServiceListDetail.as_view(), name='service-detail'),
    path('category/<int:pk>/', CategoryListDetail.as_view(), name='category-detail'),
]
