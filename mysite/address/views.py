from django.shortcuts import render
from rest_framework import viewsets,generics

from address.models import Address
from address.serializer import AddressSerializer
from rest_framework.permissions import IsAuthenticated


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)



