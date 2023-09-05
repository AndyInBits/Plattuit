from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import MicroblogPost
from .serializers import MicroblogpostSerializer


class HealthCheck(APIView):
    def get(self, request, format=None):
        return Response("OK", status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
class MicroblogpostListCreateView(APIView):
    def get(self, request):
        microblogposts = MicroblogPost.objects.all()
        serializer = MicroblogpostSerializer(microblogposts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MicroblogpostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)