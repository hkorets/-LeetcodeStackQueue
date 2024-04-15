class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        removed_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return removed_node.data

    def is_empty(self):
        return self.size == 0

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
        while self.Q1.size != 0:
            self.Q2.enqueue(self.Q1.dequeue())
        self.Q1, self.Q2 = self.Q2, self.Q1

    def pop(self) -> int:
        return self.Q1.dequeue()

    def top(self) -> int:
        return self.Q1.peek()

    def empty(self) -> bool:
        return self.Q1.is_empty()
  
