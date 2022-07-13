from django.db import models
import uuid


class RentHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    reseted = models.BooleanField(default=False)

    rent_accounts = models.ManyToManyField("rent_accounts.RentAccount", related_name="rent_accounts")
    user = models.ManyToManyField("users.User", related_name="user")
