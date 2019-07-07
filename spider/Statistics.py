import time


class Statistics:
    """Ведение статистики, собираем данные в формате prometheus
    Работает как синглтон и оборачивает как декоратор методы обращения к ресурсам и выполнения запросов
    """

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance

    def __init__(self):
        self.date = time.time()

    def __call__(self, func):
        async def wrap():
            return await func()
        return wrap
