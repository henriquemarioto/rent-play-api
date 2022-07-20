from .models import RentAccount


def rent_account_login_censorship(rent_account: RentAccount):
    return f"{rent_account.login[0]}{'*' * (len(rent_account.login)-1)}"