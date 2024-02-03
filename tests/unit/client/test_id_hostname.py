import unittest
from unittest import mock


class TestCCClient_IDHostname(unittest.TestCase):

    @mock.patch('subprocess.run', mock.MagicMock())
    def test_hostname(self):
        pass
