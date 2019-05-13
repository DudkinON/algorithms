from unittest import TestCase
from data_structures import Node
from problem_solving.linked_list.find_n_from_end import nth_from_last


class TestLinkList(TestCase):

    def gen_list(self, _from, _to):
        head = Node(_from)
        current = head

        if _from > _to:
            for i in range(_from - 1, _to - 1, -1):
                current.next = Node(i)
                current = current.next

        elif _from < _to:
            for i in range(_from + 1, _to + 1):
                current.next = Node(i)
                current = current.next

        return head

    def test_nth_from_last(self):
        head = self.gen_list(7, 1)

        result = nth_from_last(head, 1)

        self.assertEqual(result, 1)
        self.assertEqual(nth_from_last(head, 8), None)
        self.assertEqual(nth_from_last(None, 2), None)
