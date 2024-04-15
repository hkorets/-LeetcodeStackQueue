class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node(None)
        
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def is_empty(self):
        return self.head.next is None

    def peek(self):
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next  # Set the next pointer of the new node to the current top of the stack
        self.head.next = node

    def pop(self):
        remove = self.head.next
        self.head.next = self.head.next.next
        return remove.value

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()  # For enqueue operations
        self.stack2 = Stack()  # For dequeue operations

    def push(self, value):
        # Simply push the value onto stack1
        self.stack1.push(value)

    def pop(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()
        
    def empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty(
