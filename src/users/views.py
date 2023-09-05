from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics
from .serializers import MyUserProfileCreateSerializer
from rest_framework.authtoken.models import Token


class HealthCheck(APIView):
    def get(self, request, format=None):
        return Response("OK", status=status.HTTP_200_OK)


class MyUserProfileCreateView(generics.CreateAPIView):
    serializer_class = MyUserProfileCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        my_user_profile = serializer.save()

        return Response(
            {"message": "User Created"},
            status=status.HTTP_201_CREATED,
        )


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.id})
