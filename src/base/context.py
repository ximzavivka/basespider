# Объект контекста задачи
# Оборачивает задачи, исполняемые интерфейсом
# Должен работать таким образом, чтобы:
# - При асинхронной работе небыло лага между выполнениями задач
# - В любой момент можно было скормить объект контекста и сценарий вернется к старому состоянию


class Context:
    # Дерево выполнения задач
    __interface = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.playbook = dict()
        return cls.__instance

    def __init__(self, task=None):
        self.parent = None
        self.child = None

