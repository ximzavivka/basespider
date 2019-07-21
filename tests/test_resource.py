import pytest

from base.resource import Resource
from utils.exceptions import ValuesInvalid


def test_singleton():
    # Работает как singleton
    assert id(Resource()) == id(Resource())


@pytest.mark.asyncio
async def test_queue():
    # Очередь пополняется
    test_data = 'test'
    resource = Resource()
    await resource.put_task('test')
    assert await resource.get_task() == test_data


def test_validate():
    # Получение исключения при валидации
    try:
        Resource().put_task('data')
    except ValuesInvalid:
        assert True
    else:
        assert False, 'Exception не сработал'


def test_stream():
    # Проверить -- работает ли стрим
    pass
