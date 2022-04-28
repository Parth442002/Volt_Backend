from dataclasses import field
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Vehicle


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"
