from django.db import models
import uuid


class Game(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name: models.CharField(max_length=64, unique=True)
    image: models.CharField()
    release_date: models.DateField()
