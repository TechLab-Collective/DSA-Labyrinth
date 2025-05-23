class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class StackLinkedList:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        self.top = Node(item, self.top)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        popped = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped

    def peek(self):
        return self.top.data if not self.is_empty() else None

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size
