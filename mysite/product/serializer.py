from rest_framework import serializers
from django.conf import settings
from comment.models import Comment
from product.models import Product, OrderedProduct, ProductImage
from comment.serializer import CommentSerializer

class ProductImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model =ProductImage
        fields = ['url']

    def get_url(self, obj):
        return f'{settings.HOST}{obj.image.url}'


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, source='product_comments')
    images = ProductImageSerializer(many=True, source='product_images')


    class Meta:
        model = Product
        fields = ['name',
                  'type',
                  'status',
                  'unit_type',
                  'id',
                  'comments',
                  "images",
                  "price",
                  "info"
                  ]


class SerializerOrderedProduct(serializers.ModelSerializer):
    product = ProductSerializer(many=False,read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderedProduct
        fields = [
            'product',
            'count',
            'product_id',

        ]
