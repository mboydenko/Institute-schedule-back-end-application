from rest_framework.exceptions import APIException

class NameNotAvailable(APIException):
    status_code = 409
    default_code = 'Имя не доступно'
    default_detail = 'Группа с таким именем уже существует'
