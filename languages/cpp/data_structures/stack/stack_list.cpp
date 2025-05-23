#include "stack_list.h"

StackList::StackList() : top(nullptr), size(0) {}

StackList::~StackList() {
    while (top != nullptr) {
        Node* temp = top;
        top = top->next;
        delete temp;
    }
}

bool StackList::isEmpty() const {
    return top == nullptr;
}

int StackList::getSize() const {
    return size;
}

void StackList::push(int val) {
    Node* newNode = new Node(val);
    if (top == nullptr) {
        top = newNode;
    } else {
        newNode->next = top;
        top = newNode;
    }
    size++;
}

int StackList::pop() {
    if (top == nullptr) {
        throw std::runtime_error("Trying to pop an empty stack");
    }
    int val = top->data;
    Node* temp = top;
    top = top->next;
    delete temp;
    size--;
    return val;
}

int StackList::peek() const {
    if (top == nullptr) {
        throw std::runtime_error("Trying to peek an empty stack");
    }
    return top->data;
}
