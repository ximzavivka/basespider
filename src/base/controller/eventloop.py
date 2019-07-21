import asyncio
import os

import uvloop

from base.resource import Resource

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

e = os.environ.get


class StartMixin:
    RESOURCE_WORKERS = e('RESOURCE_WORKERS', 1)  # Количество потоков выполения запросов ресурса

    # Управление исполняемыми задачами и циклом выполнения
    def __set_task(self, task):
        # Включение задачи при старте
        # Проверка состояния
        if self.is_empty():
            self.__tasks.append(
                self.loop.create_task(
                    task
                )
            )

    def start_app(self):
        # Ждем запуска зависимых компонентов

        # Создание воркеров для отправки данных в ресурс
        # Они слушают очередь и выполняют сетевые запросы
        for _ in self.RESOURCE_WORKERS:
            self.__set_task(Resource(self).stream())

        # Запуск одного экземпляра сценария
        self.__set_task(self.scenario)

        # Запуск цикла
        self.loop.run_until_complete(
            asyncio.wait(
                self.__tasks
            )
        )

        self.loop.close()
