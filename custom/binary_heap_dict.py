class BinaryHeapDict(object):
    """docstring for BinaryHeapDict"""
    def __init__(self, mx=True):
        self.mx = mx
        self.L = [None]
        self.D = {}
        self.N = 0
        self.compare = self.less if mx else self.more

    def less(self, a, b):
        return self.D[self.L[a]][0] < self.D[self.L[b]][0]

    def more(self, a, b):
        return self.D[self.L[a]][0] > self.D[self.L[b]][0]

    def exch(self, i, j):
        self.L[i], self.L[j] = self.L[j], self.L[i]
        self.D[self.L[i]][1], self.D[self.L[j]][1] = i, j

    def swim(self, k):
        """Get key of each element further up the heap and access dict
        to compare values."""
        while k > 1 and self.compare(k//2, k):
            self.exch(k//2, k)
            k = k//2

    def sink(self, k):
        """Get key of each element further down the heap and access dict
        to compare values."""
        while 2*k <= self.N:
            j = 2*k
            if j < self.N and self.compare(j, j+1):
                j += 1
            if not self.compare(k, j):
                break
            self.exch(k, j)
            k = j


class PriorityQueueDict(BinaryHeapDict):
    """This data structure can handle any hashable key->value pairs
    and return them in sorted order in O(n log n). The top priority
    key-value pair can be gotten in constant time, and the value for
    any key can also be gotten in constant time. The implementation
    uses a dict backed by a list for sinking and swimming key-value
    pairs in O(log n). The priority for any element can be set
    after it has been inserted into the queue, which makes this
    data structure suitable for implementing Dijkstra's algorithm."""
    def __init__(self, mx=True):
        super(PriorityQueueDict, self).__init__(mx)

    def insert(self, key, value):
        """Insert a key->value pair into the queue. Clients
        can't insert the same key twice."""
        if key in self.D:
            self.set_priority(key, value)
            return
        self.N += 1
        self.L.append(key)
        self.D[key] = [value, self.N]
        self.swim(self.N)

    def remove_top(self):
        if self.N < 1:
            raise IndexError("There are no elements in this priority queue dict.")
        key, value = self.L[1], self.D[self.L[1]][0]
        self.exch(1, self.N)
        self.L.pop()
        self.D.pop(key)
        self.N -= 1
        self.sink(1)
        return key, value

    def peek(self):
        return (None, None) if self.N < 1 else (self.L[1], self.D[self.L[1]][0])

    def sorted_order(self):
        while self.N > 0:
            yield self.remove_top()

    def get_priority(self, key):
        """Returns priority for the given key if it exists."""
        return self.D[key][0] if key in self.D else None

    def set_priority(self, key, new_val):
        if key not in self.D:
            raise IndexError("This key is not in the queue.")
        val, index = self.D[key]
        self.D[key][0] = new_val
        self.swim(index) if self.mx == (new_val > val) else self.sink(index)

    def check_integrity(self):
        """Checks that the dict and list backing the queue agree
        on the indices for all keys."""
        for index, key in enumerate(self.L):
            if index > 0:
                assert self.D[key][1] == index





if __name__ == '__main__':

    import random

    max_pq = PriorityQueueDict()
    keys = ['a', 'all', 'been', 'blocking', 'call', 'currently', 'every', 'for', 'had', 'have', 'is', 'it', 'item', 'items', 'meaning', 'processed', 'received', 'resume', 'task_done', 'when']
    for key in keys:
        max_pq.insert(key, random.randrange(20))

    print(max_pq.D)
    print(max_pq.peek())

    max_pq.check_integrity()
    max_pq.set_priority('been', 13)
    max_pq.check_integrity()

    sorted_list = []
    for e in max_pq.sorted_order():
        sorted_list.append(e)
    print(sorted_list)
    max_pq.check_integrity()

