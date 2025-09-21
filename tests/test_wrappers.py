"""wrappers pytest suite."""

import pytest

from tools import wrappers

@pytest.mark.parametrize('n', [10, 15., 100500])
def test_retry_count(n):
    i = 0
    @wrappers.retry(count=n)
    def decorated():
        nonlocal i
        i += 1
        raise KeyError
    try:
        decorated()
    except KeyError:
        pass
    assert i == n


@pytest.mark.parametrize('c', [10, 15., 100500])
def test_retry_count_positional(c):
    i = 0
    @wrappers.retry(c)
    def decorated():
        nonlocal i
        i += 1
        raise KeyError
    try:
        decorated()
    except KeyError:
        pass
    assert i == c


@pytest.mark.parametrize('d', [None, 3, 15., 'foobarbaz', tuple, {}])
def test_retry_default(d):
    @wrappers.retry(default=d)
    def def_retry_decorated():
        raise LookupError
    assert def_retry_decorated() == d
