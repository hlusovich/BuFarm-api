from rest_framework import serializers

from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    flat = serializers.CharField(required=False)
    class Meta:

        model= Address
        fields = (
            'city',
            'street',
            'building',
            'flat',

        )
    def create(self, validated_data):
        validated_data['user']=self.context.get('request').user
        return super().create(validated_data)