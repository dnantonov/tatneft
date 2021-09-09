from rest_framework import serializers

from api.models import GasStation


class GasStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasStation
        fields = '__all__'
