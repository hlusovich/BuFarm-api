from  rest_framework import serializers

from order.models import Order
from product.serializer import SerializerOrderedProduct


class OrderSerializer(serializers.ModelSerializer):
    ordered_products = SerializerOrderedProduct(many = True,source='products')
    class Meta:
        model = Order
        fields = [
            "created_at",
            "updated_at",
            "status",
            "id",
            "ordered_products"
        ]