from collections import deque

from custom.graph import UnweightedGraph
from custom.dfo import DepthFirstOrder
# from .graph import UnweightedGraph

class SCC:
    """Runs Kosaraju-Sharir algorithm on graph
    to compute strongly connected components (sets
    of vertices for any vertex can be reached from
    any other vertex).
    """

    def __init__(self, G):
        self.G = G
        self.component = 0
        self.dfo = DepthFirstOrder(G.reverse())
        for v in G:
            v.marked = False
            v.id = None
        for v in self.dfo:
            # get vertex in G from vertex in G-R
            v = G.get_vertex(v.get_node())
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
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_vertex(7)
    g.add_vertex(8)
    g.add_vertex(9)
    g.add_vertex(10)
    g.add_vertex(11)
    g.add_vertex(12)

    # 5 strongly connected components
    g.add_edge(0,1)
    g.add_edge(0,5)
    g.add_edge(2,0)
    g.add_edge(2,3)
    g.add_edge(3,2)
    g.add_edge(3,5)
    g.add_edge(4,2)
    g.add_edge(4,3)
    g.add_edge(5,4)

    g.add_edge(6,0)
    g.add_edge(6,4)
    g.add_edge(6,8)
    g.add_edge(6,9)
    g.add_edge(8,6)

    g.add_edge(7,6)
    g.add_edge(7,9)

    g.add_edge(9,10)
    g.add_edge(9,11)
    g.add_edge(10,12)
    g.add_edge(11,4)
    g.add_edge(11,12)
    g.add_edge(12,9)

    scc = SCC(g)
    for node in g.get_nodes():
        print("node: {}, id: {}".format(node, scc.id(node)))






