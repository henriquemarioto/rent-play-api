import uuid

from django.db import models


class Platform(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    platform_api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30, unique=True)
    image_url = models.URLField(max_length=255)
    icon = models.CharField(max_length=40)
