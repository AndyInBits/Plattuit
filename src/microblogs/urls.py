from django.urls import path

from . import views

urlpatterns = [
    path("healthcheck", views.HealthCheck.as_view(), name="healthcheck"),
    path('microblogposts', views.MicroblogpostListCreateView.as_view(), name='microblogposts-list-create'),
]