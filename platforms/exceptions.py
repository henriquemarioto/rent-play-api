from rest_framework.exceptions import APIException
from rest_framework.views import status

class PlatformAlreadyExistsInDataBase(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "This platform already exists in the database!"
    default_code = "platform_exists" 