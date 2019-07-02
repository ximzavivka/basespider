from exceptions import InitException


class Request:
    """Отправка HTTP запросов"""

    def __init__(self, loop):
        if not self.check_status():
            raise InitException(self.__class__)

    # Выполни вот этот запрос, верни мне результат
    # Оберни запрос в proxy

    @classmethod
    def check_status(cls):
        # Проверка статуса в интернете
        return True
