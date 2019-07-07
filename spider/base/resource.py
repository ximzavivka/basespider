import os
import asyncio
import aiohttp

from base.statistics import Statistics

e = os.environ.get

# Ресурсы
#
# Выполняет запросы на nginx, сохраняющий данные
# Создается несколько воркеров для выполнения запросов очереди
# Очередь реализует буффер для хранения запросов


class Resource:
    """Обращение к внутренним ресурсам"""
    RESOURCE_HOST = e('RESOURCE_HOST', 'localhost')

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance

    def __init__(self, queue):
        self.loop = asyncio.get_event_loop()
        self.queue = queue

    async def wrap_request(self, request):
        """Обработка статуса, вернувшегося результата"""
        if request.status == 500:
            await asyncio.sleep(1)  # Ожидание между запросами с ошибкой
            await self.queue.put_nowait(data)

    @Statistics
    async def post(self, data):
        """Отправка данных источника"""
        await self.queue.put_nowait(data)

    @classmethod
    async def stream(cls, queue):
        """Процесс обработки очереди"""
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.post(Resource.RESOURCE_HOST, data=await queue.get_nowait()) as resp:
                    return resp
