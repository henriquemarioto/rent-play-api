from django.db import models
from django.contrib.auth.models import AbstractUser

from .utils import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = None
    nickname = models.CharField(unique=True, max_length=16)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cellphone = models.CharField(unique=True, max_length=11)
    email = models.EmailField(unique=True, max_length=255)
    wallet = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname", "first_name", "last_name"]
    objects = CustomUserManager()
