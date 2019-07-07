import os
import asyncio
import uvloop

from Resource import Resource

e = os.environ.get

queue = asyncio.Queue()


async def main(interface):
    """Цикл событий"""
    # Запустить интерфейс
    interface = interface()

    # Запустить задачу
    await interface.start()


def start_app(interface):
    # Ждем запуска зависимых компонентов
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()

    app = [main(interface)]  # Задачи вставлять сюда

    for i in range(e('RESOURCE_WORKERS', 80)):
        app.append(Resource.stream(queue))

    loop.run_until_complete(
        asyncio.wait(
            map(loop.create_task, app)
        )
    )

    loop.close()

# TODO: Подключить sentry и чтобы у используемых проектов были свои ключи
# TODO: Сделать Pip пакетом
# TODO: Подключить Jaeger
