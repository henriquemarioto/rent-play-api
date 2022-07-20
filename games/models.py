from django.db import models
import uuid


class Game(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    game_api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255, unique=True)
    image_url = models.URLField(max_length=255)
    release_date = models.DateField()

    platforms = models.ManyToManyField("platforms.Platform", related_name="platforms")
