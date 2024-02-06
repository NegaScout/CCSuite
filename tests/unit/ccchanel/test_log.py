import unittest
from parameterized import parameterized
from unittest.mock import mock_open, patch
from ccsuite.ccchanel.ccchanel_log import log_init, log_append, log_read

from tests.unit.ccchanel.base_setup_ccchanelfile_ccstenobase import TestCaseWith_CCChanelFile_CCStenoBase


class TestCCChanel_Log_Init(TestCaseWith_CCChanelFile_CCStenoBase):
    @parameterized.expand([
        ("client_id", b'[]')
    ])
    @patch('builtins.open', new_callable=mock_open)
    def test_log_init(self, client_path, should_be_writen_with, mocked_open):
        log_init(self.chanel, self.steno, client_path)
        mocked_open().write.assert_called_once_with(should_be_writen_with)


class TestCCChanel_Log_Read(TestCaseWith_CCChanelFile_CCStenoBase):

    @parameterized.expand([
        ("/tmp/client_id", [], b'[]', True)
    ])
    @patch("os.path.exists")
    def test_log_read_with_data_present(self, client_path, expected_read_data, mocked_read_data, file_present, mock_listdir):
        mock_listdir.configure_mock(return_value=file_present)
        with patch('builtins.open', new_callable=mock_open, read_data=mocked_read_data) as mocked_open:
            import os
            data_read = log_read(self.chanel, self.steno, client_path)
            self.assertEqual(expected_read_data, data_read)


class TestCCChanel_Log_Append(TestCaseWith_CCChanelFile_CCStenoBase):
    @parameterized.expand([
        ("/tmp/client_id", b'[]', "entry", b'["entry"]', True)
    ])
    @patch("os.path.exists")
    def test_log_append_with_data_present(self, client_path, data_already_present, object_to_write, expected_writen_data, file_present, mock_listdir):
        mock_listdir.configure_mock(return_value=file_present)
        with patch('builtins.open', new_callable=mock_open, read_data=data_already_present) as mocked_open:
            log_append(self.chanel, self.steno, object_to_write, client_path)
            mocked_open().write.assert_called_once_with(expected_writen_data)
