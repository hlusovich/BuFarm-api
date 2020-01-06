import mixin as mixin
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from  rest_framework import generics
from rest_framework.permissions import IsAdminUser, BasePermission,IsAuthenticated

from product.models import Product, OrderedProduct
from product.serializer import ProductSerializer, SerializerOrderedProduct


class NewIsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return bool(request.user and request.user.is_staff)
        elif request.method == 'GET' :
            return True



class ProductViewsSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [NewIsAdminUser]

class OrderedproductViewSet(viewsets.ModelViewSet):
    queryset = OrderedProduct.objects.all()
    serializer_class = SerializerOrderedProduct
    permission_classes = [IsAuthenticated]

    #def perform_create(self, serializer):
        #serializer.save(owner = self.request.user)
        #serializer.save(product = Product.id)





# Create your views here.
