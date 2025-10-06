import pytest


@pytest.fixture()
def init():
    print('init done')
    return True


@pytest.fixture()
def preset_and_clean():
    print('settings done')
    yield 'value'
    print('cleanup done')
