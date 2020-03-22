from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,max_length=20)

    class Meta:
        model = User
        fields = (
            'info',
            'first_name',
            'last_name',
            'email',
            'password',
            'id',
        )

    def validate_password(self, value: str):
        return make_password(value)

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        return super().create(validated_data)
