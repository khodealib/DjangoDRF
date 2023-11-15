from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserRegistrationSerializer, UserSerializer

User = get_user_model()


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    queryset: QuerySet = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        serializer = self.serializer_class(instance=self.queryset, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(instance=user)
        return Response(data=serializer.data)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response(data={'message': 'permission denied, you are not owner'})
        serializer = self.serializer_class(instance=user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response(data={'message': 'permission denied, you are not owner'})
        user.is_active = False
        user.save()
        return Response(data={'message': 'user deactivated.'})
