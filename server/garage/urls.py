from django.urls import path
from .views import VehicleList
urlpatterns = [
    #path('garages/', GarageList.as_view()),
    #path('vehicles', VehicleList.as_view()),
    path('vehicles/', VehicleList.as_view()),

]
