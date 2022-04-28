from rest_framework.serializers import ModelSerializer, Serializer
from .models import Vehicle, Garage


class GarageSerializer(ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'
