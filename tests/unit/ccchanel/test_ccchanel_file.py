import unittest
from parameterized import parameterized

from unittest.mock import mock_open, patch

from tests.unit.ccchanel.base_setup_ccchanelfile import TestCaseWith_CCChanelFile


class TestCCChanel_CCChanelFile_Write(TestCaseWith_CCChanelFile):

    @parameterized.expand([
        ("/tmp/client", b'data')
    ])
    @patch('builtins.open', new_callable=mock_open)
    def test_write_data(self, path, data, mocked_open):
        self.chanel.write(data, path)
        mocked_open.assert_called_once_with(path, 'wb')
        mocked_open().write.assert_called_once_with(data)

    @parameterized.expand([
        (b'data',)
    ])
    @patch('builtins.open', new_callable=mock_open)
    def test_write_data_without_path(self, data, mocked_open):
        with self.assertRaises(TypeError) as context:
            self.chanel.write(data)


class TestCCChanel_CChanelFile_Read(TestCaseWith_CCChanelFile):

    @parameterized.expand([
        ('/tmp', b'data')
    ])
    def test_read_data(self, path, wanted_data):
        with patch('builtins.open', new_callable=mock_open, read_data=wanted_data) as mocked_open:
            read_data_chanel = self.chanel.read(path)
            mocked_open.assert_called_once_with(path, 'rb')
            mocked_open().read.assert_called_once_with()
            self.assertEqual(wanted_data, read_data_chanel)


class TestCCChanel_CChanelFile_List(TestCaseWith_CCChanelFile):

    @parameterized.expand([
        ('/tmp', ['file1', 'file2'])
    ])
    @patch("os.listdir")
    def test_list_dir(self, path, wanted_listed_files, mock_listdir):
        mock_listdir.configure_mock(return_value=wanted_listed_files)
        chanel_list = self.chanel.list(path)
        mock_listdir.assert_called_once_with(path)
        self.assertEqual(wanted_listed_files, chanel_list)


class TestCCChanel_CChanelFile_Exists(TestCaseWith_CCChanelFile):

    @parameterized.expand([
        ('/tmp/file1', True)
    ])
    @patch("os.path.exists")
    def test_file_exists(self, the_file, expected_file_exists, mock_exists):
        mock_exists.configure_mock(return_value=expected_file_exists)
        file_exists = self.chanel.exists(the_file)
        self.assertEqual(file_exists, expected_file_exists)
