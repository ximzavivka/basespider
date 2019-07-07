# Собирает данные из WS
from base.interface import WS
from spider.spider import start_app


class MainInterface(WS):
    @property
    def address(self):
        return ''

    async def receiver(self, data):
        """Описание потребителя данных"""


start_app(MainInterface)
