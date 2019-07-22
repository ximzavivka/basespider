# Подключение к источникам потребления


class BaseInterface:
    def __init__(
            self,
            login=None,  # Пользователь
            password=None,  # Пароль
            base_headers=None,  # Заголовки, которые нужно передавать в каждом запросе
            auth_page=None,  # Страница авторизации

    ):
        self.login = login
        self.password = password
        self.base_headers = base_headers
        self.auth_page = auth_page

    def authenticate(self) -> dict:
        """Выполняет запрос на авторизацию
        Возвращает объект Network, с доступным методом request"""
        raise NotImplemented

    def get_iterator(self) -> tuple:
        """Должен вернуть цикл и правило итерации по циклу"""
        raise NotImplemented

    def request(self):
        pass
