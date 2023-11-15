from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserRegistrationSerializer


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
