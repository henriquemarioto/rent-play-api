from django.db import models
import uuid


class Game(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    game_api_id = models.IntegerField()
    name = models.CharField(max_length=64)
    image_url = models.URLField(max_length=255)
    release_date = models.DateField()
