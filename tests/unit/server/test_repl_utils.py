import unittest
from ccsuite.server.repl_utils import *


class TestCCServer_ReplUtils(unittest.TestCase):

    def test_repl_command(self,
                          create_function=create_repl_command_remote,
                          command_args=[['target_sample', 'command_sample', 'args_sample']],
                          obj_wanted={'kind': 'remote', 'payload': {'args': ['args_sample'], 'command': 'command_sample', 'target': 'target_sample'}}):

        obj_created = create_function(*command_args)
        self.assertDictEqual(obj_wanted, obj_created)
