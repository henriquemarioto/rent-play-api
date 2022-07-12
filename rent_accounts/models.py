from django.db import models
import uuid

class RentAccount(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    plataform = models.CharField(max_length=16)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)

    renter = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="renter", null=True
    )
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="owner"
    )

    games = models.ManyToManyField("games.Game", related_name="rent_accounts")
