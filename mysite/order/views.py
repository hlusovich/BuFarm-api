from django.http import QueryDict, request
from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings


from order.models import Order
from order.serializer import OrderSerializer




class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


    def perform_destroy(self, instance: Order):
        if instance.status == Order.CANCELED_CHOICE:
            return

        instance.status = Order.CANCELED_CHOICE
        instance.save()

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return self.retrieve(request, *args, **kwargs)


    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
# Create your views here.
