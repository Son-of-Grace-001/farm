from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

class User(AbstractUser):
    # Add any additional fields here.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)