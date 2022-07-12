from tkinter import CASCADE
from django.db import models

class Movie(models.Model):
    service = models.CharField(max_length=16)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)   
    end_date = models.DateField()
    price = models.DecimalField()    
    
    users = models.OneToOneField("users.User",on_delete=CASCADE, related_name="users")


    def __repr__(self):
        return f"Movie {self.title} - {self.duration} - {self.premiere} - {self.classification} - {self.synopsis} - {self.genres}"

