import unittest
from stack_list import StackList
from stack_deque import StackDeque
from stack_linkedlist import StackLinkedList

class StackTestCase:
    def stack_class(self):
        raise NotImplementedError

    def setUp(self):
        self.stack = self.stack_class()

    def test_push_and_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.stack.push(6)
        self.assertEqual(self.stack.peek(), 6)

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)

class TestStackList(StackTestCase, unittest.TestCase):
    def stack_class(self):
        return StackList

class TestStackDeque(StackTestCase, unittest.TestCase):
    def stack_class(self):
        return StackDeque

class TestStackLinkedList(StackTestCase, unittest.TestCase):
    def stack_class(self):
        return StackLinkedList

if __name__ == "__main__":
    unittest.main()
