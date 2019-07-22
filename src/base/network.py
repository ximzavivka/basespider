# Управляет запросами к внешним ресурсам
# HTTP, gRPC,
#
from utils.exceptions import ExternalAuthorizationFailed


class Network:
    """Интерфейс запросов по сети
    Оборачивает любой запрос
    """
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/75.0.3770.142 Safari/537.36 '

    def __init__(self):
        self.auth, self.auth_headers = self.authenticate()

    def authenticate(self):
        return '', ''

    def request(self):
        if not self.auth:
            raise ExternalAuthorizationFailed

        return self._request()

    def _request(self):
        # Здесь должен быть вызов сетевого запроса
        pass
