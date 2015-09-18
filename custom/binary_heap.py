class BinaryHeap(object):
    """docstring for BinaryHeap"""
    def __init__(self, mx=True):
        self.L = [None]
        self.N = 0
        self.compare = self.less if mx else self.more

    def less(self, a, b):
        return self.L[a] < self.L[b]

    def more(self, a, b):
        return self.L[a] > self.L[b]

    def exch(self, i, j):
        self.L[i], self.L[j] = self.L[j], self.L[i]

    def swim(self, k):
        while k > 1 and self.compare(k//2, k):
            self.exch(k//2, k)
            k = k//2

    def sink(self, k):
        while 2*k <= self.N:
            j = 2*k
            if j < self.N and self.compare(j, j+1):
                j += 1
            if not self.compare(k, j):
                break
            self.exch(k, j)
            k = j


class PriorityQueue(BinaryHeap):
    """This priority queue can handle any elements that implement
    rich comparison. It does not support keys with associated values,
    but rather only values."""
    def __init__(self, mx=True):
        super(PriorityQueue, self).__init__(mx)

    def insert(self, v):
        self.L.append(v)
        self.N += 1
        self.swim(self.N)

    def remove_top(self):
        if self.N < 1:
            raise IndexError("There are no elements in this priority queue.")
        v = self.L[1]
        self.exch(1, self.N)
        self.L.pop()
        self.N -= 1
        self.sink(1)
        return v

    def peek(self):
        return self.L[min(1, self.N)]

    def sorted_order(self):
        while self.N > 0:
            yield self.remove_top()


if __name__ == '__main__':

    import random

    max_pq = PriorityQueue()
    for i in range(100):
        max_pq.insert(random.randrange(100))

    print(max_pq.L)
    sorted_list = []
    for e in max_pq.sorted_order():
        sorted_list.append(e)
    print(sorted_list)

    print(max_pq.peek())


    min_pq = PriorityQueue(mx=False)
    for i in range(100):
        min_pq.insert(random.randrange(100))

    print(min_pq.L)
    sorted_list = []
    for e in min_pq.sorted_order():
        sorted_list.append(e)
    print(sorted_list)

    print(min_pq.peek())
    print(min_pq.remove_top())





