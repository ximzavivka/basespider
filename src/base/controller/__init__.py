# Интерфейс контроля выполнения задач

# Создает N воркеров
# Объявляется вместе со стартом работы
# Задачи на выполнение кладутся в resource_queue
# В случае 200 кода в ответ -- удаляет задание из очереди
# Работает как синглтон
# Реализует интерфейс работы с очередью
import asyncio
import os

from base.context import Context
from base.controller.eventloop import StartMixin
from base.controller.status import StatusMixin
from base.interface import BaseInterface
from base.scenario import BaseScenario
from base.statistics import Statistics

e = os.environ.get


class Controller(StatusMixin, StartMixin):

    @staticmethod
    def generate_start_token():
        # Генерация токена парсера
        return ''

    def __init__(self, interface, scenario):
        assert issubclass(interface, BaseInterface), "Интерфейс должен реализовывать базовый"
        assert issubclass(scenario, BaseScenario), "Сценарий должен реализовывать базовый"

        # Технические
        self.loop = asyncio.get_event_loop()
        self.__tasks = []
        # Логика
        self.scenario = scenario(interface=interface)  # Цикл, выполняющий логику поведения
        self.statistics = Statistics(self)  # Объект для записи статистики
        # Механика
        self.network_iterator = None
        self.token = self.generate_start_token()
        self.status = "EMPTY"
        self.queue = asyncio.Queue()

    async def get_task(self):
        # Получение сетевого задания
        # Проверить состояние
        return await self.queue.get()

    async def set_task(self, task):
        # Поставить сетевую задачу
        # Проверить состояние
        assert issubclass(task, Context), "Поставленные задачи должны быть обернуты в контекст"

        return await self.queue.put_nowait(task)
