from rest_framework import serializers

from comment.models import Comment
from product.models import Product, OrderedProduct
from comment.serializer import CommentSerializer

class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, source='product_comments')

    class Meta:
        model = Product
        fields = ['name',
                  'type',
                  'status',
                  'unit_type',
                  'id',
                  'comments'
                  ]


class SerializerOrderedProduct(serializers.ModelSerializer):
    order_id=serializers.IntegerField(write_only=True)
    product = ProductSerializer(many=False,read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderedProduct
        fields = [
            'product',
            'count',
            'order_id',
            'product_id',
        ]
