class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        removed_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_node.data

    def is_empty(self):
        return self.head == None

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

class MyStack:
    def __init__(self):
        self.Q1 = Queue()
        self.Q2 = Queue()

    def push(self, x: int) -> None:
        self.Q2.enqueue(x)
        while not self.Q1.is_empty():
            self.Q2.enqueue(self.Q1.dequeue())
        self.Q1, self.Q2 = self.Q2, self.Q1

    def pop(self) -> int:
        return self.Q1.dequeue()

    def top(self) -> int:
        return self.Q1.peek()

    def empty(self) -> bool:
        return self.Q1.is_empty()
  
