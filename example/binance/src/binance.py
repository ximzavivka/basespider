# Собирает данные из WS
from Interface import WS
from spider.spider import start_app


class MainInterface(WS):
    @property
    def address(self):
        return ''

    def receiver(self):
        """Описание потребителя данных"""


async def task_generator():
    pass

start_app(main, interface=MainInterface)
