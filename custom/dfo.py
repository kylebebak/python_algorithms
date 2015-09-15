from custom.graph import UnweightedGraph

class DepthFirstOrder:
    """Runs DFS on graph in order to return
    reverse DFS postorder of graph, useful
    for finding strongly connected components
    in the graph. DFS is implemented recursively
    instead of using a stack.
    """
    def __init__(self, G):
        self.G = G
        self.post = []
        for v in G:
            v.marked = False
        for v in G:
            if not v.marked:
                self.dfs(G, v)

    def dfs(self, G, source):
        source.marked = True
        for v in source.get_neighbors():
            if not v.marked:
                self.dfs(G, v)
        self.post.append(source)

    def __iter__(self):
        return iter(reversed(self.post))



if __name__ == '__main__':
    g = UnweightedGraph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_vertex(7)
