from django.db import models


class RentHistory(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    reseted = models.BooleanField(default=False)

    rent_accounts = models.ManyToManyField(
        "rent_accounts.RentAccount",
        related_name="rent_accounts",
        on_delete=models.DO_NOTHING,
    )
    user = models.ManyToManyField(
        "users.User", related_name="user", on_delete=models.DO_NOTHING
    )
