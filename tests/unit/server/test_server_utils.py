import unittest
from unittest import mock

from ccsuite.server.server_utils import *


class TestCCServer_ServerUtils_GetLastPing(unittest.TestCase):
    def test_last_ping(self,
                       cclog=[{'alive': {'timestamp': 1704385737}}, {'ping': {'timestamp': 1704385758}}],
                       obj_wanted={'timestamp': 1704385758}):
        created_command_object = get_last_ping(cclog)
        self.assertDictEqual(obj_wanted, created_command_object)


class TestCCServer_ServerUtils_IsOnline(unittest.TestCase):

    @mock.patch('time.time', mock.MagicMock(return_value=1704385758))
    def test_is_online(self,
                       cclog=[{'alive': {'timestamp': 1704385737}}, {'ping': {'timestamp': 1704385758}}],
                       mocked_timestamp=1704385758,
                       is_online_wanted=True,
                       age_treshold=30):
        is_online_result = is_online(cclog, age_treshold=age_treshold)
        self.assertEqual(is_online_wanted, is_online_result)
