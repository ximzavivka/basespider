import os
import asyncio
import aiohttp

from Statistics import Statistics

e = os.environ.get

# Ресурсы
#
# Получение данных / отправка результатов происходит через NGINX
# NGINX принимает запросы, занимается балансировкой и содержанием коннектов к ресурсам
#
# Дескриптор оборачивает запросы, расшифровывет результаты


class Resource:
    """Обращение к внутренним ресурсам"""
    RESOURCE_HOST = e('RESOURCE_HOST', 'localhost')

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance

    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.queue = asyncio.Queue()

    def __call__(self, *args, **kwargs):
        while True:
            task = self.queue.get_nowait()

    def read_status(self, status):
        """Обработка статуса, вернувшегося результата"""
        if status == 500:
            pass

    @Statistics()
    async def post(self, data):
        """Отправка данных источника"""
        async with aiohttp.ClientSession() as session:
            async with session.post(Resource.RESOURCE_HOST) as resp:
                self.read_status(resp.status)

    async def stream(self):
        """Процесс обработки очереди"""
        pass
