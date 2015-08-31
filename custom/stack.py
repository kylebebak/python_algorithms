class Node:
    def __init__(self, value, nxt=None, prv=None):
        self.value = value
        self.nxt = nxt
        self.prv = prv

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        n = Node(value, self.head)
        self.head = n
        self.size += 1

    def pop(self):
        value = self.head.value
        self.head = self.head.nxt
        self.size -= 1
        return value

