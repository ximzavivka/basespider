import os
import asyncio
import uvloop

e = os.environ.get


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

    loop.run_until_complete(
        asyncio.wait([
            # Задачи вставлять сюда, обернутые в loop.create_task
            loop.create_task(
                main(interface)
            )
        ])
    )

    loop.close()

# TODO: Подключить sentry и чтобы у используемых проектов были свои ключи
# TODO: Сделать Pip пакетом
# TODO: Подключить Jaeger
