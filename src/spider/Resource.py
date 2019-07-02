import asyncio
import os

from spider.Network import Request

e = os.environ.get

# Ресурсы
#
# Получение данных / отправка результатов происходит через NGINX
# NGINX принимает запросы, занимается балансировкой и содержанием коннектов к ресурсам
#
# Дескриптор оборачивает запросы, расшифровывет результаты


class Resource:
    """Дескриптор для обращение к ресурсам
    Обертывает работу с NGINX как api-gateway
    """
    RESOURCE_HOST = 'localhost'

    def __init__(self, loop):
        self.network = Request(loop)
        self.queue = asyncio.Queue()

    def get(self, url, params: dict, method="GET"):
        """Получить данные с внешнего ресурса"""
        pass

