import unittest
from unittest import mock

from ccsuite.ccchanel.ccchanel_messages import *


class TestCCChanel_Messeges(unittest.TestCase):
    @mock.patch('time.time', mock.MagicMock(return_value=12345))
    def test_server_command(self,
                            command_kind='exec',
                            command_args=('test',),
                            obj_wanted={'command': {'args': ['test'], 'id': 12345, 'kind': 'exec', 'timestamp': 12345}}):
        created_command_object = message_create_command(command_kind, *command_args)
        self.assertDictEqual(obj_wanted, created_command_object)
