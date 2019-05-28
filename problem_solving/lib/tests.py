from unittest import TestCase
from problem_solving.lib.binary import add_binary


class TestBinary(TestCase):

    def test_add_binary(self):
        self.assertEqual(add_binary(b'0000', b'0000'), '0')
        self.assertEqual(add_binary(b'0001', b'0010'), '11')
        self.assertEqual(add_binary(b'0010', b'10000'), '10010')
        self.assertEqual(add_binary(b'0111', b'0001'), '1000')
        self.assertEqual(add_binary(b'1111', b'1111'), '11110')
