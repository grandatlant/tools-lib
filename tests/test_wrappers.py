"""wrappers pytest suite."""

import pytest

#wrappers = None
from tools import wrappers


@pytest.fixture(scope='session')
def wrap_all_tests():
    print('Init before tests.')
    yield
    print('Cleanup after all tests in session.')


def test_import_success(wrap_all_tests):
    assert wrappers is not None


@pytest.mark.parametrize('n', [10, 15.])
def test_retry_count(init, n):
    assert init
    i = 0
    @wrappers.retry(count=n, exceptions=KeyError)
    def decorated():
        nonlocal i
        i += 1
        raise KeyError
    try:
        decorated()
    except KeyError:
        pass
    assert i == n


@pytest.mark.parametrize('c', [10, 15.])
def test_retry_count_positional(preset_and_clean, c):
    i = 0
    @wrappers.retry(c, exceptions=KeyError)
    def decorated():
        nonlocal i
        i += 1
        raise KeyError
    try:
        decorated()
    except KeyError:
        pass
    assert i == c


@pytest.mark.parametrize('d', [None, 3, 15., 'foobarbaz', tuple, {'1': 1}])
def test_retry_default(d):
    @wrappers.retry(default=d, exceptions=LookupError)
    def def_retry_decorated():
        raise LookupError
    assert def_retry_decorated() == d


@pytest.mark.skip('Skipped test.')
def test_skip():
    assert False


if __name__ == '__main__':
    pytest.main()
