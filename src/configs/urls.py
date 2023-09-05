from django.urls import include, path

urlpatterns = [
    path("api/v1/blog/", include("microblogs.urls")),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/interations/", include("interations.urls")),
    path("api/v1/tracking/", include("trackings.urls")),
    
]
