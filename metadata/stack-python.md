# Stack in Python

## Description:
This is a simple implementation of the **Stack** data structure in Python. The stack follows the **Last In, First Out (LIFO)** principle, where elements are added and removed from the top of the stack. This implementation supports the basic stack operations such as:

- **push**: Adds an item to the top of the stack.
- **pop**: Removes and returns the top item of the stack.
- **peek**: Returns the top item without removing it.
- **is_empty**: Checks if the stack is empty.
- **size**: Returns the number of elements in the stack.

## Language:
Python

## File Path:
`languages/python/data_structures/stack.py`

---

## Example Usage:

```python
# Example usage of the Stack class

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
print(stack.peek())  # Output: 10
print(stack.is_empty())  # Output: False
```

## Complexity:
- push: O(1)
- pop: O(1)
- peek: O(1)
- is_empty: O(1)
- size: O(1)