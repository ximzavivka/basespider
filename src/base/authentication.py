# Процесс авторизации

# Работает почти по принципу oauth2
# При запуске скрипт отправляет информацию о себе
# Что нужно учитывать:
# - Токен задачи
# - Токен автора
# - Версия скрипта
# - Версия basedocker
# - Билд скрипта
# - Билд basedocker
# В ответ получает: access_token == JWT
# access_token передается в HTTP заголовке, при обращении к ресурсам
# На стороне api-gateway проверяется и проксируется на нужный ресурс
import asyncio
import jwt

from utils.exceptions import ResourceUnavailable, InternalAuthorizationFailed


class Authentication:
    """Система аутентификаци/авторизации
    Оборачивает запросы к ресурсам"""
    AUTHOR = None

    LIBRARY_VERSION = None
    VERSION = None

    LIBRARY_BUILD = None
    BUILD = None

    AUTH_HOST = None  # Сервер авторизации
    ACCESS_TOKEN = None
    PUBLIC_KEY = None

    def __init__(self):
        """Выполняет аутентификацию
        Проверяем заданные параметры аутентификации
        Генерирует токен задачи/процесса
        """
        self.access_token = None
        self.public_key = None
        self.loop = asyncio.get_event_loop()

    @classmethod
    def check_resource(cls):
        # Проверка статуса ресурса, обрабазывающего запросы авторизации
        raise ResourceUnavailable

    @classmethod
    def get_public_key(cls):
        cls.check_resource()
        return ''

    @classmethod
    async def get_token(cls):
        # Получение токена из AUTH_HOST
        # Если не получится -- вызвать исключение
        raise InternalAuthorizationFailed

    @classmethod
    async def authentication(cls):
        # Идентификация пользователя
        # Получить токен
        return await cls.get_token()

    async def check_access_token(self):
        # Валидировать токен авторизации
        # Если с ним что-то не так -- сбросить на None
        if not self.public_key:
            self.public_key = Authentication.get_public_key()

        if self.access_token:
            try:
                jwt.decode(self.access_token, self.public_key, algorithms='RS256', verify=True)
            except (
                    jwt.InvalidTokenError,
                    jwt.DecodeError,
                    jwt.InvalidSignatureError,
                    jwt.ExpiredSignatureError,
                    jwt.InvalidAudienceError,
                    jwt.InvalidIssuerError,
                    jwt.InvalidIssuedAtError,
                    jwt.ImmatureSignatureError
            ):
                self.access_token = None

    async def authorization(self):
        # Процесс проверки прав
        await self.check_access_token()
        if not self.access_token:
            self.access_token = await self.authentication()


def authentication(func):
    async def wrap(*args, **kwargs):
        await Authentication().authentication()
        return await func(*args, **kwargs)

    return wrap
