class Vertex:
    """A vertex that maintains a dict of (vertex -> weight)
    key-value pairs of neighbors to which it is connected.
    This avoids needing an extra data type, EDGE, to represent
    connections between vertices."""
    def __init__(self, node):
        self.node = node
        self.adjacent = {}

    def __repr__(self):
        """Override this to print a string representation of
        this object."""
        return str(self.node)

    def print(self):
        print(self.node, "->", self.adjacent)

    def get_node(self):
        return self.node

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_neighbors(self):
        return self.adjacent.keys()

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class UnweightedVertex(Vertex):
    """A vertex that maintains a list of vertices to which it is connected,
    instead of a dict with vertices and their corresponding weights. The
    implementation can also use a set of vertices instead of a list, which
    removes the ability to have parallel edges, but which speeds up queries
    for whether vertex_a is a neighbor of vertex_b."""
    def __init__(self, node):
        self.node = node
        self.adjacent = []

    def add_neighbor(self, neighbor):
        self.adjacent.append(neighbor)

    def get_neighbors(self):
        return self.adjacent



class Graph:
    """A collection of vertices connected by edges
    to their neighbors. The vertices are maintained
    in a dict of (node -> vertex) key-value pairs."""
    def __init__(self, vertices=None):
        self.vertices = ({} if vertices is None else vertices)

    def __iter__(self):
        """Returns all vertex instances in vertices dict."""
        return iter(self.vertices.values())

    def add_vertex(self, node):
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        return new_vertex

    # returns keys instead of values
    def get_nodes(self):
        return self.vertices.keys()

    def get_vertex(self, node):
        try:
            return self.vertices[node]
        except:
            return None

    def size(self):
        return len(self.vertices)

    def has_vertex(self, node):
        return node in self.vertices

    def add_edge(self, frm, to, cost=0, both=False):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)

        self.vertices[frm].add_neighbor(self.vertices[to], cost)
        if both:
            self.vertices[to].add_neighbor(self.vertices[frm], cost)

class UnweightedGraph(Graph):
    """UnweightedVertex instances are stored instead of Vertex instances."""
    def add_vertex(self, node):
        new_vertex = UnweightedVertex(node)
        self.vertices[node] = new_vertex
        return new_vertex

    def add_edge(self, frm, to, both=False):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)

        self.vertices[frm].add_neighbor(self.vertices[to])
        if both:
            self.vertices[to].add_neighbor(self.vertices[frm])

    def reverse(self):
        """Reverse (frm -> to) for neighbors of each
        vertex in graph."""
        reversed_vertices = {}
        for node, vertex in self.vertices.items():
            reversed_vertices[node] = UnweightedVertex(node)
        for v in self.vertices.values():
            for u in v.get_neighbors():
                reversed_vertices[u.get_node()].add_neighbor(
                    reversed_vertices[v.get_node()]
                )
        return UnweightedGraph(reversed_vertices)


if __name__ == '__main__':

    g = UnweightedGraph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)


    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    g.add_edge(3, 4)
    g.add_edge(5, 2)
    g.add_edge(5, 1)
    g.add_edge(1, 5)

    print("graph")
    for v in g:
        v.print()

    print("\nreverse of graph")
    rg = g.reverse()
    for v in rg:
        v.print()





