"""wrappers pytest suite."""

import unittest

#wrappers = None
from tools import wrappers


class RetryTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(repr(cls), 'setUpClass call')

    def setUp(self):
        print('setUp call')

    def tearDown(self):
        print('tearDown call')

    def test_import_success(self):
        assert wrappers is not None

    def test_retry_count(self):
        n = 100500
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

    def test_retry_count_positional(self):
        c = 140
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

    def test_retry_default(self):
        d = 'abcde'
        @wrappers.retry(default=d, exceptions=LookupError)
        def def_retry_decorated():
            raise LookupError
        assert def_retry_decorated() == d


if __name__ == '__main__':
    unittest.main()
