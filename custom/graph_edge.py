from .mixins import ComparableHashableMixin

class Edge(ComparableHashableMixin):
    """Comparable, and hence sortable, edge data type for
    connecting a pair of vertices in a graph."""
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __repr__(self):
        return '{0} -> {1}, weight: {2}'.format(self.v, self.w, self._weight)

    def either(self):
        return self.v

    def other(self, vertex):
        """The vertex not passed to this method."""
        return self.w if vertex == self.v else self.v

    def get_weight(self):
        return self.weight

    def __lt__(self, other):
        return self.get_weight() < other.get_weight()


class EdgeWeightedGraph:
    """A weighted, undirected graph. Self loops and parallel edges are
    permitted. Vertices are represented by an indexed list. Each element
    in the vertex list is a set of edges pointing to adjacent vertices.
    """
    def __init__(self, V):
        self.V = V
        self._adj = [set() for i in range(self.V)]
        self._edges = set()

    def add_edge(self, e):
        v = e.either()
        w = e.other(v)
        self._adj[v].add(e)
        self._adj[w].add(e)
        self._edges.add(e)

    def adj(self, v):
        """Returns a generator to iterate over edges adjacent to vertex v."""
        for e in self._adj[v]:
            yield e

    def edges(self):
        """Returns a generator to iterate over all edges."""
        for e in self._edges:
            yield e

    def print(self):
        """Print edges for any vertex in the graph containing edges.
        Assumes Edge type has defined suitable __repr__()."""
        for i, v in enumerate(self._adj):
            if v:
                print('vertex {0}'.format(i))
                for e in v:
                    print(e)
                print()

