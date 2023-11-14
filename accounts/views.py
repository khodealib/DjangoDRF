from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserRegisterSerializer


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.POST)
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
