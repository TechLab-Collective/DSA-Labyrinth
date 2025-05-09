# Stack (Python)

This directory contains multiple implementations of the Stack data structure in Python.

## Implementations

- `stack_list.py` – using Python built-in list
- `stack_deque.py` – using `collections.deque` (better performance)
- `stack_linkedlist.py` – using custom linked list

## Methods

Each stack supports:

- `push(item)`
- `pop()`
- `peek()`
- `is_empty()`
- `size()`

## Running Tests

```bash
python -m unittest discover -s languages/python/data_structures/stack/tests
