import os
import asyncio
import aiohttp

from base.statistics import Statistics
from utils.exceptions import ValuesInvalid

e = os.environ.get

# Ресурсы

# Создает N воркеров
# Объявляется вместе со стартом работы
# Задачи на выполнение кладутся в resource_queue
# В случае 200 кода в ответ -- удаляет задание из очереди
# Работает как синглтон
# Реализует интерфейс работы с очередью


def validate(func):
    def wrap(*args, **kwargs):
        data = kwargs.get('data', None)
        if not data:
            raise ValuesInvalid

        return func(*args, **kwargs)
    return wrap


class Resource:
    """Обращение к внутренним ресурсам"""
    RESOURCE_HOST = e('RESOURCE_HOST', 'localhost')
    __queue = None

    # Первичная валидация поступающих данных
    # Упаковка данных в HTTP
    # Чтение кодов ответа

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__queue = asyncio.Queue(maxsize=1200)

        return cls.__instance

    def __init__(self):
        self.loop = asyncio.get_event_loop()

    async def get_task(self):
        return await self.__queue.get()

    @validate
    async def put_task(self, data=None):
        return await self.__queue.put_nowait(data)

    @classmethod
    async def wrap_request(cls, request):
        """Обработка статуса, вернувшегося результата"""
        if request.status == 500:
            await asyncio.sleep(1)  # Ожидание между запросами с ошибкой

    async def __post(self, data):
        """Отправка данных источника"""
        await self.queue.put_nowait(data)

    @classmethod
    async def stream(cls):
        """Процесс обработки очереди"""
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.post(Resource.RESOURCE_HOST, data=await Resource().get_task()) as resp:
                    return resp
