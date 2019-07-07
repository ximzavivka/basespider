# Подключение к источникам потребления


class BaseInterface:
    @property
    def address(self):
        """Полный адресс источника"""
        raise NotImplementedError

    def receiver(self):
        raise NotImplementedError

    def __receiver(self):
        await self.receiver()


class WS(BaseInterface):
    """Интерфейс для ws подключения к источнику"""


class Http(BaseInterface):
    """Интерфейс для http запросов"""
