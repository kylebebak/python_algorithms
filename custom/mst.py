from .union_find import UF
from heapq import heappush, heappop

class KruskalMST:
    """Accepts an EdgeWeightedGraph object and finds
    the minimum spanning tree/forest for this graph.
    Makes use of UF data structure to determine whether
    two vertices are already connected."""
    def __init__(self, G):
        self.G = G
        self.mst = []
        self.pq = []
        for e in G.edges():
            heappush(self.pq, e)

        self.uf = UF(G.V)
        while len(self.pq) and len(self.mst) < G.V-1:
            e = heappop(self.pq)
            v = e.either()
            w = e.other(v)
            if not self.uf.connected(v, w):
                self.uf.union(v, w)
                self.mst.append(e)

    def edges(self):
        return (self.mst)

    def connected(self, v, w):
        """Are these vertices connected?"""
        return self.uf.connected(v, w)
