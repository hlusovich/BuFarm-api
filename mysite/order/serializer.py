from  rest_framework import serializers

from order.models import Order
from product.models import OrderedProduct
from product.serializer import SerializerOrderedProduct


class OrderSerializer(serializers.ModelSerializer):
    ordered_products = SerializerOrderedProduct(many=True, source='products')
    address_id=serializers.IntegerField(write_only=True)
    class Meta:
        model = Order
        fields = [
            "created_at",
            "updated_at",
            "status",
            "id",
            "ordered_products",
            "address_id"
        ]

    def create(self, validated_data):
        ordered_products=validated_data.pop('products')
        order =Order.objects.create(**validated_data)
        for i in ordered_products:
            OrderedProduct.objects.create(count=i.get("count"),
            product_id=i.get("product_id"),order = order)
        return order

