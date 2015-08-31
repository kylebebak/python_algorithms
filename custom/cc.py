from collections import deque

from custom.graph import UnweightedGraph
# from .graph import UnweightedGraph

class CC:
    """Runs DFS repeatedly on vertices of graph
    until all connected components have been found."""

    def __init__(self, G):
        self.G = G
        self.component = 0
        for v in G:
            v.marked = False
            v.id = None
        for v in G:
            if not v.marked:
                v.marked = True
                v.id = self.component
                self.dfs(G, v)
                self.component += 1

    def dfs(self, G, source):
        q = deque([source])
        while len(q):
            u = q.pop()
            for v in u.get_neighbors():
                if not v.marked:
                    v.marked = True
                    v.id = self.component
                    q.append(v)

    def count(self):
        return self.component

    def id(self, node):
        return self.G.get_vertex(node).id

    def connected(self, node_a, node_b):
        return self.id(node_a) == self.id(node_b)



if __name__ == '__main__':
    g = UnweightedGraph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_vertex(7)

    g.add_edge(1,2, both=True)
    g.add_edge(2,4, both=True)
    g.add_edge(2,6, both=True)

    g.add_edge(3,5, both=True)


    cc = CC(g)
    for node in g.get_nodes():
        print("node: {}, id: {}".format(node, cc.id(node)))

    for node in g.get_nodes():
        print("node 1 is connected to node {}: {}".format(node, cc.connected(1, node)))






