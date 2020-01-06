from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny

from user.models import User
from user.serializer import UserSerializer

class NewPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            return bool(request.user and request.user.is_authenticated)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(UserViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        return self.retrieve(self.request)

    def get_object(self):
        return self.queryset.get(username=self.request.user)

    def get_queryset(self):
        return self.queryset.get(username=self.request.user)#поговорить про реквест

# Create your views here.
