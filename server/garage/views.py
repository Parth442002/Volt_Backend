from .serializers import VehicleSerializer
from rest_framework import generics
from rest_framework import permissions
from .models import Vehicle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class VehicleList(generics.ListCreateAPIView):
    '''
    Vehicle List and Create View for the end User
    '''
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        final_array = []
        responses = Vehicle.objects.filter(owner=request.user)
        for response in responses:
            data = VehicleSerializer(response)
            final_array.append(data.data)

        return Response(final_array)
