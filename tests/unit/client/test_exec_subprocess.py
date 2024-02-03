import unittest
from unittest import mock


class TestCCClient_ExecSubprocess(unittest.TestCase):

    @mock.patch('subprocess.run', mock.MagicMock())
    def test_exec(self):
        pass
