import uuid

from django.db import models


class Platform(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=16)
    image_url = models.URLField(max_length=255)
    