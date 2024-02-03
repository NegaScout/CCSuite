import unittest
from ccsuite.steno.steno_base import CCStenoBase
from ccsuite.ccchanel.ccchanel_file import CCChanelFile


class TestCaseWith_CCChanelFile_CCStenoBase(unittest.TestCase):
    def setUp(self):
        self.chanel = CCChanelFile()
        self.steno = CCStenoBase()