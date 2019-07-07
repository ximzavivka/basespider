import time


class Statistics:
    """Ведение статистики, собираем данные в формате prometheus
    Работает как синглтон и оборачивает как декоратор методы обращения к ресурсам и выполнения запросов
    """
    def __init__(self):
        self.date = time.time()

    def __call__(self, func):
        async def wrap():
            return await func()
        return wrap
