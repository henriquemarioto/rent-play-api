from rest_framework.exceptions import APIException
from rest_framework.views import status

class KeyIsRequired(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Wallet field is required"
    default_code = "wallet_required" 

class WalletWithoutFunds(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Wallet not enough funds!"
    default_code = "wallet_not_funds" 