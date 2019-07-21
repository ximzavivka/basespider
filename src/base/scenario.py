# Сценарий принимает в качестве


class BaseScenario:
    INTERFACE = None

    def __new__(cls, interface=None):
        if not cls.INTERFACE:
            cls.INTERFACE = interface

        return super().__new__(cls)

    def __init__(self):
        pass
