from django.db import models

# Create your models here.
class User(models.Model):    
    nickname = models.CharField(unique=True, max_length=16)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cellphone = models.CharField(unique=True, max_length=11)
    email = models.EmailField(unique=True, max_length=255)
    wallet = models.DecimalField(max_digits=8, decimal_places=2, default=0)

  
