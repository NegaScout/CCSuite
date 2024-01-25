import unittest
from unittest.mock import mock_open, patch
from ccsuite.ccchanel.ccchanel_file import CCChanelFile


class TestCCChanelWrite(unittest.TestCase):
    def setUp(self):
        self.chanel = CCChanelFile()

    @patch('builtins.open', new_callable=mock_open)
    def test_write_data(self, mock_open, path='/tmp/client', data=b'data'):
        self.chanel.write(data, path)
        mock_open.assert_called_once_with(path, 'wb')
        mock_open().write.assert_called_once_with(data)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_data_without_path(self, mock_open, data=b'data'):
        with self.assertRaises(TypeError) as context:
            self.chanel.write(data)


class TestCCChanelRead():
    def test_list_files(self, remote_path_to_list=''):
        pass


class TestCCChanelList():
    def test_list_files(self, remote_path_to_list=''):
        pass
