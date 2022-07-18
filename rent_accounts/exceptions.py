from rest_framework.exceptions import APIException
from rest_framework.views import status

class EmailAlreadyExistInThisPlatform(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "This platform already has an account with this email!"
    default_code = "email_exists" 