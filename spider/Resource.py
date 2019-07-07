import asyncio
import os

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

    def __init__(self, loop):
        self.queue = asyncio.Queue()

    def get(self, url, params: dict, method="GET"):
        """Получить данные с внешнего ресурса"""
        pass

