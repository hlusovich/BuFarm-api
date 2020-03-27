from  rest_framework import  serializers

from comment.models import Comment
from user.serializer import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = (
            'text',
            'user',
            'product_id',
            'id',
            'name'

        )

        def create(self, validated_data):
            validated_data['user'] = self.context.get('request').user
            return super().create(validated_data)