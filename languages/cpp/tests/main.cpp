#include <iostream>
#include <cassert>
#include "../data_structures/stack/stack_list.h"

int main() {
    StackList stack;

    assert(stack.isEmpty() && "Stack should be empty initially");

    stack.push(10);
    assert(!stack.isEmpty() && "Stack should not be empty after push");
    assert(stack.peek() == 10 && "Top should be 10");

    stack.push(20);
    assert(stack.peek() == 20 && "Top should now be 20");

    stack.pop();
    assert(stack.peek() == 10 && "Top after pop should be 10");

    stack.pop();
    assert(stack.isEmpty() && "Stack should be empty after popping all elements");

    try {
        stack.pop();
        assert(false && "Expected exception for pop on empty stack");
    } catch (const std::underflow_error&) {}

    try {
        stack.peek();
        assert(false && "Expected exception for peek on empty stack");
    } catch (const std::underflow_error&) {}

    std::cout << "✅ All stack tests passed!\n";
    return 0;
}
