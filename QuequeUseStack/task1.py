class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        node = Node(x)
        if self.tail is None:
            self.head = self.tail = node
        self.tail.next = node
        self.tail = node 

    def pop(self) -> int:
        node = self.head
        self.head = node.next
        return node.data

    def peek(self) -> int:
        return self.head.data

    def empty(self) -> bool:
        if self.head is None:
            return True
        return False
