from django.db import models
from django.contrib.auth.models import AbstractUser

from .utils import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=255)
    nickname = models.CharField(unique=True, max_length=16)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_seller = models.BooleanField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname", "first_name", "last_name"]
    objects = CustomUserManager()
