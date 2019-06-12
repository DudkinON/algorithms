from unittest import TestCase
from data_structures import Node
from problem_solving.linked_list.find_n_from_end import nth_from_last
from problem_solving.linked_list.merge import merge_lists
from problem_solving.linked_list import remove_duplicates
from problem_solving.linked_list import remove_node
from problem_solving.linked_list.sum import sum_lists
from problem_solving.linked_list.palindrome import is_palindrome
from problem_solving.linked_list import intersection
from problem_solving.linked_list import loop_detection


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

    def gen_list_from_array(self, lst):
        head = tail = Node(lst[0])

        for i in range(1, len(lst)):
            node = Node(lst[i])
            tail.next = node
            tail = tail.next

        return head

    def get_list(self, _from, _to, step):
        head = tail = Node(_from)
        for num in range(_from + step, _to + 1, step):
            tail.next = tail = Node(num)

        return head

    def test_nth_from_last(self):
        head = self.gen_list(7, 1)

        result = nth_from_last(head, 1)

        self.assertEqual(result, 1)
        self.assertEqual(nth_from_last(head, 8), None)
        self.assertEqual(nth_from_last(None, 2), None)

    def test_merge_lists(self):

        node = merge_lists(self.get_list(1, 5, 2), self.get_list(2, 4, 2))
        val = 1
        while node:
            self.assertEqual(node.value, val)
            val += 1
            node = node.next

    def check(self, h, e):

        while h and e:
            self.assertEqual(h.value, e.value)
            h = h.next
            e = e.next

    def test_remove_duplicates(self):

        head = self.gen_list_from_array([1, 1, 2, 3, 4, 5, 2])
        expect = self.gen_list_from_array([1, 2, 3, 4, 5])
        remove_duplicates(head)
        self.check(head, expect)

        del head
        del expect

        head = self.gen_list_from_array([0, 0])
        expect = self.gen_list_from_array([0])

        self.check(head, expect)

        del head
        del expect

        head = expect = self.gen_list_from_array([0])

        self.check(head, expect)

    def test_remove_node(self):

        head = expect = self.gen_list_from_array([1, 2, 3])
        node = Node(0)
        child = head.next
        head.next = node
        node.next = child
        self.check(head, self.gen_list_from_array([1, 0, 2, 3]))
        remove_node(node)
        self.check(head, expect)

        del node
        del head
        del expect

        head = expect = self.gen_list_from_array([1])
        node = Node(10)
        head.next = node
        self.check(head, self.gen_list_from_array([1, 10]))
        remove_node(node)
        self.check(head, expect)

    def test_sum_lists(self):

        a = self.gen_list_from_array([7, 1, 6])
        b = self.gen_list_from_array([5, 9, 2])
        expect = self.gen_list_from_array([2, 1, 9])

        result = sum_lists(a, b)

        self.check(result, expect)

        del a, b, expect

        a = self.gen_list_from_array([0])
        b = self.gen_list_from_array([1, 2])
        expect = self.gen_list_from_array([1, 2])

        result = sum_lists(a, b)
        self.check(result, expect)

    def test_is_palindrome(self):

        ll = self.gen_list_from_array([1, 2, 3, 4, 5, 4, 3, 2, 1])
        self.assertEqual(True, is_palindrome(ll))

        del ll

        ll = self.gen_list_from_array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(False, is_palindrome(ll))

        del ll

        ll = self.gen_list_from_array([0])

        self.assertEqual(True, is_palindrome(ll))

    def test_intersection(self):

        a = self.gen_list_from_array([1, 2, 3])
        b = self.gen_list_from_array([4, 5, 6])

        self.assertEqual(None, intersection(a, b))

        a.next.next.next = b

        self.assertEqual(b, intersection(a, b))

    def test_loop_detection(self):

        ll = self.gen_list_from_array([1, 2, 3, 4, 5, 6])

        self.assertEqual(loop_detection(ll), None)

        node = ll

        while node:
            if node.next is None:
                node.next = ll.next
                break
            node = node.next

        self.assertEqual(loop_detection(ll), ll.next)
