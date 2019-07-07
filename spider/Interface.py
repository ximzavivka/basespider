# Подключение к источникам потребления
import asyncio

from Authentication import Authentication, authentication
from Resource import Resource


class BaseInterface:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.resource = Resource()
        self.authentication = Authentication()

    @property
    def address(self):
        """Полный адресс источника
        Этот адресс берется для объявления источника"""
        raise NotImplementedError

    async def start(self):
        """Запуск цикла событий"""
        raise NotImplementedError

    async def receiver(self, data):
        """Что делать, когда получаешь данные"""

        raise NotImplementedError

    @authentication
    async def __receiver(self, *args, **kwargs):
        """Обертка для получения данных и отправки в ресурс"""
        await self.resource.post(await self.receiver(*args, **kwargs)) # Отправка данных


class WS(BaseInterface):
    """Интерфейс для ws подключения к источнику"""
    async def start(self):
        pass


class HTTP(BaseInterface):
    """Интерфейс для http запросов"""
