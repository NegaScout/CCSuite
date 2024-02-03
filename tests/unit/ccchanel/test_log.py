import unittest
from unittest.mock import mock_open, patch
from ccsuite.ccchanel.ccchanel_log import log_init, log_append, log_read
from ccsuite.ccchanel.ccchanel_file import CCChanelFile
from ccsuite.steno.steno_base import CCStenoBase


# todo inherit from common CCChanel class to omit setUp
class TestCCChanel_Log_Init(unittest.TestCase):
    def setUp(self):
        self.chanel = CCChanelFile()
        self.steno = CCStenoBase()

    @patch('builtins.open', new_callable=mock_open)
    def test_log_init(self, mock_open, path='/tmp/client'):
        log_init(self.chanel, path, self.steno)
        mock_open().write.assert_called_once_with(b'[]')


class TestCCChanel_Log_Read(unittest.TestCase):
    def setUp(self):
        self.chanel = CCChanelFile()
        self.steno = CCStenoBase()

    @patch("os.listdir", return_value=['client'])
    @patch('builtins.open', new_callable=mock_open, read_data=b'[]')
    def test_log_read_with_data_present(self, mock_open, mock_listdir, path='/tmp/client', expected_read_data=[]):
        data_read = log_read(self.chanel, path, self.steno)
        self.assertEqual(expected_read_data, data_read)


class TestCCChanel_Log_Append(unittest.TestCase):
    def setUp(self):
        self.chanel = CCChanelFile()
        self.steno = CCStenoBase()

    @patch("os.listdir", return_value=['client'])
    @patch('builtins.open', new_callable=mock_open, read_data=b'[]')
    def test_log_append_with_data_present(self, mock_open, mock_listdir, path='/tmp/client', expected_writen_data=b'["entry"]'):
        log_append(self.chanel, path, 'entry', self.steno)
        mock_open().write.assert_called_once_with(expected_writen_data)
