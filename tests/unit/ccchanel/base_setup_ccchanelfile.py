import unittest
from ccsuite.ccchanel.ccchanel_file import CCChanelFile


class TestCaseWith_CCChanelFile(unittest.TestCase):
    def setUp(self):
        self.chanel = CCChanelFile()
