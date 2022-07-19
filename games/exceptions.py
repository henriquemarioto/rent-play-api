from rest_framework.exceptions import APIException
from rest_framework.views import status

class GameAlreadyExistsInDataBase(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "This game already exists in the database!"
    default_code = "game_exists" 