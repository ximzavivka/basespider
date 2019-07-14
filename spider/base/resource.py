import os
import asyncio
import aiohttp

from base.authentication import authentication
from base.statistics import Statistics
from utils.exceptions import ValuesInvalid, ResourceFail

e = os.environ.get

# Ресурсы

# Создает N воркеров
# Объявляется вместе со стартом работы
# Задачи на выполнение кладутся в resource_queue
# В случае 200 кода в ответ -- удаляет задание из очереди
# Работает как синглтон
# Реализует интерфейс работы с очередью


def validate(func):
    async def wrap(obj, data):
        if not data:
            raise ValuesInvalid()

        return await func(obj, data)
    return wrap


class Resource:
    """Обращение к внутренним ресурсам"""
    RESOURCE_HOST = e('RESOURCE_HOST', 'localhost')
    __instance = None

    # Первичная валидация поступающих данных
    # Упаковка данных в HTTP
    # Чтение кодов ответа

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__instance.__queue = asyncio.Queue(maxsize=1200)

        return cls.__instance

    def __init__(self):
        pass

    @authentication
    async def get_task(self):
        return await self.__queue.get()

    @validate
    async def put_task(self, data):
        return await self.__queue.put_nowait(data)

    async def __post(self, data):
        """Отправка данных источника"""
        await self.__queue.put_nowait(data)

    @Statistics  # Сохранение статистики
    async def check_response(self, response):
        pass

    @check_response
    async def finalizer(self, response):
        try:
            await self.check_response(response)
        except ResourceFail:
            pass
        else:
            self.__queue.task_done()

    @classmethod
    async def stream(cls):
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.post(Resource.RESOURCE_HOST, data=await cls().get_task()) as resp:
                    await cls().finalizer(resp)
