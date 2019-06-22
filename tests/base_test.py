import unittest


class BaseUnitTest(unittest.TestCase):

    _test_class = None

    def test_cmd(self):
        self._test_class.cmd()