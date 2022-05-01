from django.contrib.auth import get_user_model
from django.db import models

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

CONNECTOR_TYPE = (
    ('Type 1', 'Type 1')
    ('Type 2', 'Type 2')
    ('Type 3', 'Type 3')
    ('Type 4', 'Type 4')
)


class Vehicle(models.Model):
    owner = models.ForeignKey(user_model, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=200, choices=VEHICLE_TYPE)

    vehicle_company = models.CharField(
        max_length=200, choices=VEHICLE_COMPANIES, null=True, blank=True)

    vehicle_name = models.CharField(max_length=200, null=False, blank=False)

    vehicle_connector = models.CharField(
        choices=CONNECTOR_TYPE, max_length=200, blank=True, null=True)

    def __str__(self):
        if self.owner.username:
            return self.owner.username + ' '+self.vehicle_name
        elif self.owner.email:
            return self.owner.email + ' '+self.vehicle_name
