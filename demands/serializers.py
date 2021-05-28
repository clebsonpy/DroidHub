from .models import Demands, Address

from django.utils import timezone as tz

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class DemandSerializer(WritableNestedModelSerializer):

    address = AddressSerializer(many=False, required=True)

    class Meta:
        model = Demands
        fields = ['id', 'user', 'description', 'status', 'date_open', 'date_finish', 'address']
        extra_kwargs = {
            'date_finish': {'read_only': True},
            'status': {'read_only': True}
        }

    def validate_date_open(self, values):

        if values > tz.now().date():
            raise serializers.ValidationError(
                "A data de de abertura de demanda não pode ser depois de hoje!"
            )

        return values
