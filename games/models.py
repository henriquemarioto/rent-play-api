from django.db import models


class Game(models.Model):
    name: models.StringField(max_length=64, unique=True)
    image: models.StringField()
    release_date: models.DateField()


rent_accounts = models.ManyToManyField("rent_accounts", related_name="rent_accounts")
