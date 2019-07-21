import os

from base.controller import Controller

e = os.environ.get

# TODO: Подключить sentry и чтобы у используемых проектов были свои ключи
# TODO: Сделать Pip пакетом
# TODO: Подключить Jaeger


def start_app(interface=None, scenario=None):
    Controller(interface=interface, scenario=scenario).start_app()
