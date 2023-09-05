from django.urls import path

from . import views

urlpatterns = [
    path("healthcheck", views.HealthCheck.as_view(), name="healthcheck"),
    path('create_user', views.MyUserProfileCreateView.as_view(), name='create_user'),
    path('login', views.CustomObtainAuthToken.as_view(), name='login_user'),

]