class InitException(Exception):
    def __init__(self, expression):
        self.expression = expression
        self.message = "Компонент не доступен"


class AuthorizationFailed(Exception):
    def __init__(self, expression):
        self.expression = expression
        self.message = "Авторизация компонента недоступна"


class ResourceUnavailable(Exception):
    def __init__(self, expression):
        self.expression = expression
        self.message = "Ресурс не доступен"


class ValuesInvalid(Exception):
    def __init__(self, expression):
        self.expression = expression
        self.message = "Ресурс не доступен"
