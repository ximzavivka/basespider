class InitException(Exception):
    def __init__(self, expression):
        self.expression = expression
        self.message = "Компонент не доступен"


class InternalAuthorizationFailed(Exception):
    def __init__(self, expression):
        self.expression = expression
        self.message = "Авторизация компонента недоступна"


class ExternalAuthorizationFailed(Exception):
    def __init__(self):
        self.message = "Перед запросом нужно авторизовать сеть"


class ResourceUnavailable(Exception):
    def __init__(self, expression):
        self.expression = expression
        self.message = "Ресурс не доступен"


class ValuesInvalid(Exception):
    def __init__(self):
        self.message = "Ресурс не доступен"


class ResourceFail(Exception):
    def __init__(self):
        self.message = "Ресурс вернул отказ добавления данных"
