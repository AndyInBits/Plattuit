from django.contrib.auth.models import User
from users.models import MyUserProfile 
from rest_framework_simplejwt.authentication import JWTAuthentication


class JWTUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwt_auth = JWTAuthentication()
        print(jwt_auth.authenticate(request))
        user, _ = jwt_auth.authenticate(request)

        if user:
            request.user = user

            try:
                request.user_profile = MyUserProfile.objects.get(user=user)
            except MyUserProfile.DoesNotExist:
                request.user_profile = None

        response = self.get_response(request)
        return response
