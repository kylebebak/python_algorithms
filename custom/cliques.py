from collections import deque

from custom.graph import UnweightedGraph
# from .graph import UnweightedGraph

class Cliques:
    """Finds all maximal cliques in a graph. A clique
    is a group of vertices for which every pairwise
    permutation is connected in both directions. The
    algorithm works by starting with a vertex and
    recursively visiting its neighbors, adding a neighbor
    to the clique is there is a two-way connection
    between the neighbor and all vertices currently in
    the clique."""

    def __init__(self, G, min_size=2):
        self.cliques = set()
        self.min_size = min_size
        for v in G:
            self.clique_dfs(G, v)
        # keep only cliques of sufficient size
        aux = set()
        for clique in self.cliques:
            if len(clique) >= min_size:
                aux.add(clique)
        self.cliques = aux

    def clique_dfs(self, G, source):
        q = deque([source])
        clique = set()
        clique.add(source)
        while len(q):
            u = q.pop()
            for v in u.get_neighbors():
                if not v in clique:
                    for member in clique:
                        # warning: depending on the implementation of get_neighbors, the following
                        # line may require comparisons linear in the number of neighbors
                        if member not in v.get_neighbors() or v not in member.get_neighbors():
                            break
                    else:
                        clique.add(v)
                        q.append(v)
        self.cliques.add(frozenset(clique))

    def count(self):
        return len(self.cliques)

    def get_cliques(self):
        return self.cliques



if __name__ == '__main__':
    g = UnweightedGraph()
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


    # 4 cliques in total, of size, 3, 2, 4, and 3
    g.add_edge(1,2)
    g.add_edge(2,1)
    g.add_edge(1,3)
    g.add_edge(3,1)
    g.add_edge(2,3)
    g.add_edge(3,2)

    g.add_edge(3,4)
    g.add_edge(4,3)

    g.add_edge(4,5)

    g.add_edge(5,6)
    g.add_edge(5,7)
    g.add_edge(5,8)
    g.add_edge(6,5)
    g.add_edge(6,7)
    g.add_edge(6,8)
    g.add_edge(7,5)
    g.add_edge(7,6)
    g.add_edge(7,8)
    g.add_edge(8,5)
    g.add_edge(8,6)
    g.add_edge(8,7)

    g.add_edge(7,8)
    g.add_edge(7,9)
    g.add_edge(8,7)
    g.add_edge(8,9)
    g.add_edge(9,7)
    g.add_edge(9,8)

    g.add_edge(9,10)

    g.add_edge(11,10)



    cl = Cliques(g)
    print(cl.count())
    for clique in cl.get_cliques():
        print(clique)
