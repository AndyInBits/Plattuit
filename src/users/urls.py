from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

urlpatterns = [
    path("healthcheck", views.HealthCheck.as_view(), name="healthcheck"),
    path("create_user", views.MyUserProfileCreateView.as_view(), name="create_user"),
    path(
        "login", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  
    path(
        "token/refresh", TokenRefreshView.as_view(), name="token_refresh"
    ),  
    path(
        "token/verify", TokenVerifyView.as_view(), name="token_verify"
    ),  
]
