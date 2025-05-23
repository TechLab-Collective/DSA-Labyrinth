#include "stack_list.h"
#include <stdexcept>

StackList::StackList() : topNode(nullptr) {}

StackList::~StackList() {
    while (!isEmpty()) {
        pop();
    }
}

void StackList::push(int val) {
    Node* newNode = new Node(val);
    newNode->next = topNode;
    topNode = newNode;
}

void StackList::pop() {
    if (isEmpty()) throw std::underflow_error("Stack underflow");
    Node* temp = topNode;
    topNode = topNode->next;
    delete temp;
}

int StackList::peek() const {
    if (isEmpty()) throw std::underflow_error("Stack is empty");
    return topNode->data;
}

bool StackList::isEmpty() const {
    return topNode == nullptr;
}
