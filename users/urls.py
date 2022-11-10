from django.urls import path
from .views import UserDetailAPIView, RegisterUserAPIView, UsersListAPI

urlpatterns = [
    path("users/<int:id>", UserDetailAPIView.as_view()),
    path("users", UsersListAPI.as_view()),
    path('register', RegisterUserAPIView.as_view()),
]
