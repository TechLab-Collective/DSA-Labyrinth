# Stack Implementations in Python

This directory contains three different implementations of the **Stack** data structure:

## 📦 Implementations

### 1. `StackList`
- Backed by Python’s built-in `list`
- Fast and simple for most use cases
- LIFO behavior via `append()` and `pop()`

### 2. `StackDeque`
- Uses `collections.deque`
- Optimized for fast O(1) push/pop from both ends
- Safer for performance in large-scale usage

### 3. `StackLinkedList`
- Custom implementation using linked list nodes
- Good for understanding underlying pointer manipulation
- No limit on capacity

## 🧪 Tests
Unit tests are provided in `../../tests/test_stack.py` covering:
- `push()`, `pop()`, `peek()`
- `is_empty()`
- `size()`

## 📈 Complexity

| Operation  | List | Deque | LinkedList |
|------------|------|-------|------------|
| Push       | O(1) | O(1)  | O(1)       |
| Pop        | O(1) | O(1)  | O(1)       |
| Peek       | O(1) | O(1)  | O(1)       |
| Size       | O(1) | O(1)  | O(1)       |