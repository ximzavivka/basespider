# Сценарий -- базовый класс, над которым выполняются действия парсера
# Сценарий апроксимирует методы объекта Network и более мелкие сценарии
# Принимает на вход ноду дерева, которая должна исполниться


class BaseScenario:
    __instance = None
    INTERFACE = None

    def __new__(cls, interface=None):
        if not cls.__instance:
            cls.__instance = super(BaseScenario, cls).__new__()

            if not cls.INTERFACE:
                cls.INTERFACE = interface

        return cls.__instance

    def __init__(self):
        self.iterator = self.get_iterator()
        self.auth_headers = self.INTERFACE.authentication()

    def authentication(self):
        return

    async def __aiter__(self):
        return self

    async def __anext__(self):
        """Возвращает объект типа Resource"""
        pass

    def get_iterator(self):
        """

        """
        # Должен вернуть объект с интерфейсом итератора
        # Возвращаемые объекты должны быть типа: Context
        return self.INTERFACE.get_iterator()

    async def _start(self):
        # Запускает работу сценария

        raise NotImplemented
