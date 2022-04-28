from dataclasses import field
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Vehicle, Garage


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class GarageSerializer(ModelSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)

    class Meta:
        model = Garage
        fields = ['owner', 'vehicles']
