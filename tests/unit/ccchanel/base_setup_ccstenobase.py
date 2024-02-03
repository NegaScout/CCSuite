import unittest
from ccsuite.steno.steno_base import CCStenoBase


class TestCaseWith_CCStenoBase(unittest.TestCase):
    def setUp(self):
        self.steno = CCStenoBase()
