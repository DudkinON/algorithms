from unittest import TestCase
from greedy_algorithms.huffman_codes import huffman_encode
from greedy_algorithms.huffman_codes.decode import huffman_decode


class TestHuffman(TestCase):

    def test_huffman_encode(self):
        self.assertEqual(huffman_encode("a"), {'a': '0'})
        self.assertEqual(huffman_encode(""), {})
        self.assertEqual(huffman_encode("abacabad"), {'a': '0',
                                                      'b': '10',
                                                      'c': '110',
                                                      'd': '111'})

    def test_huffman_decode(self):
        prepare = {'a': '0', 'b': '10', 'c': '110', 'd': '111'}
        code = '01001100100111'
        self.assertEqual(huffman_decode({'a': '0'}, '0'), 'a')
        self.assertEqual(huffman_decode(prepare, code), 'abacabad')
