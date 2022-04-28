from pyexpat import model
from secrets import choice
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

user_model = get_user_model()

VEHICLE_TYPE = (
    ('Four Wheeler', 'Four Wheeler'),
    ('Two Wheeler', 'Two Wheeler'),
)

VEHICLE_COMPANIES = (
    ('Tata', 'Tata'),
    ('MG', 'MG'),
    ('Mahindra', 'Mahindra'),
    ('Porsche', 'Porsche'),
    ('Nissan', 'Nissan'),
    ('Jaguar', 'Jaguar'),
    ('Mini Cooper', 'Mini Cooper'),
    ('BMW', 'BMW'),
    ('Audi', 'Audi'),
    ('Mercedes', 'Mercedes'),
    ('Byd', 'Byd')
)


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=200, choices=VEHICLE_TYPE)

    vehicle_company = models.CharField(
        max_length=200, choices=VEHICLE_COMPANIES, null=True, blank=True)

    vehicle_name = models.CharField(max_length=200, null=False, blank=False)

    vehicle_connector = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.vehicle_name


class Garage(models.Model):
    owner = models.OneToOneField(user_model, on_delete=models.CASCADE)
    vehicles = models.ManyToManyField(Vehicle)

    def __str__(self):
        if self.owner.username:
            return self.owner.username+"'s Garage"
        elif self.owner.email:
            return self.owner.email+"'s Garage"
        elif self.owner.phone:
            return self.owner.phone+"'s Garage"
