import datetime, uuid
from django.db import models
import uuid

class RentHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    rent_account = models.ForeignKey(
        "rent_accounts.RentAccount", on_delete=models.CASCADE, related_name="rent_histories"
    )
    renter = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="rent_histories"
    )
