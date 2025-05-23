#ifndef STACK_LIST_H
#define STACK_LIST_H

class StackList {
private:
    struct Node {
        int data;
        Node* next;
        Node(int val) : data(val), next(nullptr) {}
    };

    Node* topNode;

public:
    StackList();
    ~StackList();

    void push(int val);
    void pop();
    int peek() const;
    bool isEmpty() const;
};

#endif
