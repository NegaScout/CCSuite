import unittest
from unittest.mock import mock_open, patch
from ccsuite.steno.steno_base import CCStenoBase


class TestCCStenoEncode(unittest.TestCase):
    def setUp(self):
        self.steno = CCStenoBase()

    def test_encode(self, object_to_encode=['test_string'], encoded_bytes=b'["test_string"]'):
        encoded_object = self.steno.encode(object_to_encode)
        self.assertEqual(encoded_object, encoded_bytes)


class TestCCStenoDecode(unittest.TestCase):
    def setUp(self):
        self.steno = CCStenoBase()

    def test_decode(self, object_to_decode=b'["test_string"]', decoded_object=['test_string']):
        decoded_object = self.steno.decode(object_to_decode)
        self.assertEqual(decoded_object, decoded_object)
