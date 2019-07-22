import os
import aiohttp

from base.authentication import authentication
from utils.exceptions import ValuesInvalid, ResourceFail

e = os.environ.get

# Ресурсы

# Дескриптор для работы с внешними ресурсами
# Оборачивает работу, выполняет авторизацию/ведение статистики/исполнение Promise
# Читает коды, регистрирует ответы ресурсов
# Общается с контроллером, для исполнения задач сети


def validate(func):
    async def wrap(obj, data):
        if not data:
            raise ValuesInvalid()

        return await func(obj, data)
    return wrap


class Resource:
    """Оборачивает дерево Context и выполняет все запросы, которые содержаться в нем"""
    RESOURCE_HOST = e('RESOURCE_HOST', 'localhost')

    def __init__(self, controller):
        self.controller = controller

    @authentication
    async def get_task(self):
        return await self.controller.get_task()

    @validate
    async def put_task(self, data):
        return await self.__queue.put_nowait(data)

    async def __post(self, data):
        """Отправка данных источника"""
        await self.__queue.put_nowait(data)

    #@Statistics  # Сохранение статистики
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

    async def stream(self):
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.post(
                        self.RESOURCE_HOST,
                        #headers=authentication(),
                        data=await self.get_task()
                ) as resp:
                    await self.finalizer(resp)
