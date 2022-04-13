from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import ProfileManager
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Profile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=20, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    mobile = models.CharField(
        max_length=10, unique=True, blank=True, null=True)

    total_kms = models.IntegerField(default=0)
    total_charging_sess = models.IntegerField(default=0)

    emailVerified = models.BooleanField(default=False)
    mobileVerified = models.BooleanField(default=False)

    # BASIC REQUIRED
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ProfileManager()

    def __str__(self):
        if self.email:
            return self.email
        elif self.mobile:
            return self.mobile
        else:
            return self.username

    @property
    def profile_verified(self):
        if self.emailVerified == True or self.mobileVerified == True:
            return True
        return False
