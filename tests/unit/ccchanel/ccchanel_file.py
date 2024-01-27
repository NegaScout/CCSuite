import unittest
from unittest.mock import mock_open, patch
from ccsuite.ccchanel.ccchanel_file import CCChanelFile


# todo inherit from common CCChanel class to omit setUp
class TestCCChanel_CCChanelFile_Write(unittest.TestCase):
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


class TestCCChanel_CChanelFile_Read(unittest.TestCase):
    def setUp(self):
        self.chanel = CCChanelFile()

    # todo parametrize
    @patch("builtins.open", new_callable=mock_open, read_data=b'data')
    def test_read_data(self, mock_open, path='/tmp'):
        read_data_chanel = self.chanel.read(path)
        mock_open.assert_called_once_with(path, 'rb')
        mock_open().read.assert_called_once_with()
        self.assertEqual(read_data_chanel, b'data')


class TestCCChanel_CChanelFile_List(unittest.TestCase):
    def setUp(self):
        self.chanel = CCChanelFile()

    # todo parametrize
    @patch("os.listdir", return_value=['file1', 'file2'])
    def test_list_dir(self, mock_listdir, path='/tmp'):
        chanel_list = self.chanel.list(path)
        mock_listdir.assert_called_once_with(path)
        self.assertEqual(chanel_list, ['file1', 'file2'])


class TestCCChanel_CChanelFile_Exists(unittest.TestCase):
    def setUp(self):
        self.chanel = CCChanelFile()

    # todo parametrize
    @patch("os.listdir", return_value=['file1', 'file2'])
    def test_file_exists(self, mock_listdir, the_file='file1', expected_exists=True):
        file_exists = self.chanel.exists(the_file)
        self.assertEqual(file_exists, expected_exists)
