from heapq import heapify, heappop, heappush
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(string):
    """
    Get string and return dictionary with codes
    :param string:
    :return: dict
    """
    heap = []
    for char, count in Counter(string).items():
        heap.append((count, len(heap), Leaf(char)))

    heapify(heap)

    counter = len(heap)
    while len(heap) > 1:
        count_one, _count_one, left = heappop(heap)
        count_two, _count_two, right = heappop(heap)
        heappush(heap, (count_one + count_two, counter, Node(left, right)))
        counter += 1

    code = {}
    if heap:
        [(fq, _count, root)] = heap
        root.walk(code, "")

    return code


def main():
    string = raw_input()
    code = huffman_encode(string)
    encoded = "".join(code[character] for character in string)
    print(len(code), len(encoded))
    for char in sorted(code):
        print("%s: %s" % (char, code[char]))

    print(encoded)


if __name__ == '__main__':
    main()
