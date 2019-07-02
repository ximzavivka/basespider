import asyncio
import os

import uvloop

from aiohttp import web

from spider.Resource import Resource

e = os.environ.get


def start_app(app):
    # Ждем запуска зависимых компонентов
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()

    loop.run_until_complete(
        asyncio.wait([
            # Задачи вставлять сюда, обернутые в loop.create_task
            loop.create_task(
                app(
                    loop,
                    aiohttp=web.Application(loop=loop),
                    resource=Resource(loop)
                )
            )
        ])
    )

    loop.close()
