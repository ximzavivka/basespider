# Интерфейс контроля выполнения задач

# Создает N воркеров
# Объявляется вместе со стартом работы
# Задачи на выполнение кладутся в resource_queue
# В случае 200 кода в ответ -- удаляет задание из очереди
# Работает как синглтон
# Реализует интерфейс работы с очередью
import asyncio
import os

import uvloop

from base.controller.status import StatusMixin
from base.interface import BaseInterface
from base.resource import Resource
from base.scenario import BaseScenario
from base.statistics import Statistics

e = os.environ.get

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class Controller(StatusMixin):
    RESOURCE_WORKERS = e('RESOURCE_WORKERS', 1)  # Количество потоков выполения запросов ресурса

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
        # Логические
        self.interface = interface  # Интерфейс реализует команды, используемые сценарием
        self.scenario = scenario  # Цикл, выполняющий логику поведения
        self.statistics = Statistics(self)  # Объект для записи статистики
        # Механика
        self.network_iterator = None
        self.token = self.generate_start_token()
        self.status = "EMPTY"

    def set_task(self, task):
        # Включение задачи при старте
        # Проверка состояния
        if self.is_empty():
            self.__tasks.append(
                self.loop.create_task(
                    task
                )
            )

    async def get_task(self):
        return await asyncio.sleep(1)

    def start_app(self):
        # Ждем запуска зависимых компонентов

        # Создание воркеров для отправки данных в ресурс
        # Они слушают очередь и выполняют сетевые запросы
        for _ in self.RESOURCE_WORKERS:
            self.set_task(Resource(self).stream())

        # Запуск одного экземпляра сценария
        self.set_task(self.scenario)

        # Запуск цикла
        self.loop.run_until_complete(
            asyncio.wait(
                self.__tasks
            )
        )

        self.loop.close()
