import time

# Реализует синглтон
# Сохраняет результаты в себе
# Скидывает буфер при заполнении


class Statistics:
    """Ведение статистики, собираем данные в формате prometheus
    Работает как синглтон и оборачивает как декоратор методы обращения к ресурсам и выполнения запросов
    """

    def __init__(self, controller):
        self.date = time.time()
        self.controller = controller
