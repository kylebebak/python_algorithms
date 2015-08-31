class Node:
    def __init__(self, value, nxt=None, prv=None):
        self.value = value
        self.nxt = nxt
        self.prv = prv

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        n = Node(value)
        if self.head:
            self.head.nxt = n
            n.prv = self.head
        else:
            self.tail = n
        self.head = n
        self.size += 1

    def append_left(self, value):
        n = Node(value)
        if self.tail:
            self.tail.prv = n
            n.nxt = self.tail
        else:
            self.head = n
        self.tail = n
        self.size += 1

    def pop(self):
        value = self.head.value
        self.head = self.head.prv
        if self.head:
            self.head.nxt = None
        else:
            self.tail = None
        self.size -= 1
        return value

    def pop_left(self):
        value = self.tail.value
        self.tail = self.tail.nxt
        if self.tail:
            self.tail.prv = None
        else:
            self.head = None
        self.size -= 1
        return value

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.prv

    def reverse(self):
        head = self.head
        self.head = self.tail
        self.tail = head

        node = self.head
        while node is not None:
            nxt = node.nxt
            node.nxt = node.prv
            node.prv = nxt
            node = nxt



if __name__ == '__main__':

    d = Deque()
    d.append(6)
    d.append(8)
    d.append(7)
    print(d.pop())
    print(d.pop())
    print(d.pop())

    d.append(6)
    d.append(8)
    d.append(7)
    print(d.pop_left())
    print(d.pop_left())
    print(d.pop_left())


    d.append(6)
    d.append(8)
    d.append(7)
    for e in d:
        print(e)

    d.reverse()
    for e in d:
        print(e)
