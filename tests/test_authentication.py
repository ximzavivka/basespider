# Обернуть запрос декоратор

from base.authentication import Authentication, authentication
from utils.exceptions import AuthorizationFailed


@authentication
async def func():
    pass


def test_singleton():
    # Проверить работу как синглтона
    assert id(Authentication()) == id(Authentication())


def test_authentication_denied():
    # Проверить отказ аутентификации
    try:
        func()
    except AuthorizationFailed:
        assert True
    else:
        assert False, "Ошибки авторизации не было"


def test_jwt_decode(public_key):
    pass

# Проверить отказ авторизации
# Проверить заполнение access_token
