class UF(object):
    """Weighted union find with path compression. Find operations are
    effectively constant time because the height of the tree grows as
    order log * N, i.e. < 5 for any reasonable N."""
    def __init__(self, N):
        self.id = [i for i in range(N)]
        self.sz = [1 for i in range(N)]

    def root(self, i):
        """Finds the root of the given node, compressing
        the path along the way."""
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        """Join p's subtree to q's subtree at their roots, so
        that the elements in these subtrees are connected."""
        if p == q:
            return
        i = self.root(p)
        j = self.root(q)
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
