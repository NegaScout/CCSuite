import unittest
from io import StringIO
from pyfakefs.fake_filesystem_unittest import TestCase as FakeFSTestCase
from ccsuite.ccchanel.ccchanel_file import CCChanelFile
from ccsuite.server.server_base import CCServer
from ccsuite.steno.steno_base import CCStenoBase


class TestCCServer_ServerBase(FakeFSTestCase):
    def setUp(self):
        self.setUpPyfakefs()

    def test_run(self, log_root_dir='/tmp/ccsuite', command_input=''):
        self.fs.create_file(log_root_dir)
        server = CCServer(CCChanelFile(), CCStenoBase(), input_stream=StringIO(command_input), log_root_dir=log_root_dir)
        server.run()
