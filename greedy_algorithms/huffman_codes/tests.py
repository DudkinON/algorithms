from unittest import TestCase
from greedy_algorithms.huffman_codes import huffman_encode


class TestHuffman(TestCase):

    def test_huffman_encode(self):
        self.assertEqual(huffman_encode("a"), {'a': '0'})
        self.assertEqual(huffman_encode(""), {})
        self.assertEqual(huffman_encode("abacabad"), {'a': '0',
                                                      'b': '10',
                                                      'c': '110',
                                                      'd': '111'})
