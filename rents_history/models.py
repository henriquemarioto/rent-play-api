import datetime, uuid
from django.db import models
import uuid


class RentHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
<<<<<<< HEAD
    start_date = models.DateField(default=datetime.date.today)
=======
    start_date = models.DateField()
>>>>>>> a69e6231de8739a433716e0f9ef9d7cf990f030c
    end_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    reseted = models.BooleanField(default=False)

    rent_accounts = models.ManyToManyField("rent_accounts.RentAccount", related_name="rent_accounts")
    user = models.ManyToManyField("users.User", related_name="user")
