# Подключение к источникам потребления
from base.resource import Resource


class BaseInterface:
    def __init__(self):
        pass

    @property
    def address(self):
        """Полный адресс источника"""
        raise NotImplementedError

    async def start(self):
        """Запуск цикла событий"""
        raise NotImplementedError

    async def receiver(self, data):
        """Что делать, когда получаешь данные"""
        raise NotImplementedError

    async def __receiver(self, *args, **kwargs):
        """Обертка для получения данных и отправки в ресурс"""
        await Resource().put_task(await self.receiver(*args, **kwargs))


class WS(BaseInterface):
    """Интерфейс для ws подключения к источнику"""
    async def start(self):
        await self.__receiver()


class HTTP(BaseInterface):
    """Интерфейс для http запросов"""
    async def start(self):
        pass
