import os
import asyncio
import uvloop

from base.interface import WS, BaseInterface
from base.resource import Resource

e = os.environ.get


class SimpleInterface(WS):
    @property
    def address(self):
        return ''

    async def receiver(self, data):
        """Описание потребителя данных"""


async def main(interface):
    """Цикл событий"""
    # Запустить интерфейс
    interface = interface()

    # Запустить задачу
    await interface.start()


def start_app(interface: BaseInterface = WS):
    # Ждем запуска зависимых компонентов
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()

    app = [main(interface)]  # Задачи вставлять сюда

    # Создание воркеров для отправки данных в ресурс
    [app.append(loop.create_task(Resource.stream())) for i in range(e('RESOURCE_WORKERS', 1))]

    loop.run_until_complete(
        asyncio.wait(
            map(loop.create_task, app)
        )
    )

    loop.close()


if __name__ == '__main__':
    start_app()

# TODO: Подключить sentry и чтобы у используемых проектов были свои ключи
# TODO: Сделать Pip пакетом
# TODO: Подключить Jaeger
