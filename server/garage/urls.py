from django.urls import path
from .views import GarageList, VehicleList
urlpatterns = [
    path('garages/', GarageList.as_view()),
    path('vehicles', VehicleList.as_view()),
]
