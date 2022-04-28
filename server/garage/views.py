from .serializers import GarageSerializer, VehicleSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Garage, Vehicle


class GarageList(generics.ListCreateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
    permission_classes = [AllowAny]


class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [AllowAny]
