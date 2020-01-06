from  rest_framework import  serializers

from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = (
            'text',
            'user',
            'product_id'
        )