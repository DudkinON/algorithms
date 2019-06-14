from unittest import TestCase
from problem_solving.stack import Stack


class TestStack(TestCase):
    def test_stack(self):

        # create an empty stack
        stack = Stack()

        # make sure stack does'n throw an error if called method `pop`
        self.assertEqual(stack.pop(), None)

        # create a stack and initialise first number
        stack = Stack(8)

        # test that stack initialised property min
        self.assertEqual(stack.min, 8)

        # call method `pop` stack is empty
        self.assertEqual(stack.pop(), 8)

        # put a few numbers on the stack
        stack.push(6)
        stack.push(4)
        stack.push(7)
        stack.push(2)

        # make sure that stack returns correct min property
        self.assertEqual(stack.min, 2)
        stack.pop()
        self.assertEqual(stack.min, 4)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.min, 6)

        # call `pop` method (remove last number)
        self.assertEqual(stack.pop(), 6)

        # make sure that stack is empty and don't contains any values
        self.assertEqual(stack.is_empty(), True)
        self.assertEqual(stack.min, None)
        self.assertEqual(stack.pop(), None)

