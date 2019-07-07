import asyncio
import os

import uvloop

e = os.environ.get


async def app():
    pass


def start_app(appinterface=None, iterator=None):
    # Ждем запуска зависимых компонентов
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()

    loop.run_until_complete(
        asyncio.wait([
            # Задачи вставлять сюда, обернутые в loop.create_task
            loop.create_task(
                app()
            )
        ])
    )

    loop.close()

# TODO: Подключить sentry и чтобы у используемых проектов были свои ключи
# TODO: Сделать Pip пакетом
# TODO: Подключить Jaeger
