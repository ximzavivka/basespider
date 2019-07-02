# Обернуть запрос декоратор

from spider.Authentication import Authentication, authentication
from exceptions import AuthorizationFailed


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

# Проверить отказ авторизации
# Проверить заполнение access_token
# Проверить поведение при устаревании ключа
