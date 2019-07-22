# Объект контекста задачи
# Оборачивает задачи, исполняемые интерфейсом
# Должен работать таким образом, чтобы:
# - В любой момент можно было скормить объект контекста и сценарий вернется к старому состоянию


class BaseContext:
    # Дерево выполнения задач
    __interface = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.playbook = dict()
        return cls.__instance

    def __init__(self):
        pass


class Context(BaseContext):
    pass
