import unittest
from custom.graph_edge import Edge, EdgeWeightedGraph
from custom.mst import KruskalMST

class TestUF(unittest.TestCase):
    """This unit test includes the EdgeWeightedGraph
    data type."""
    def setUp(self):
        vertices = [
            {1:16,2:12,3:21},
            {3:17,4:20},
            {3:28,5:31},
            {4:18,5:19,6:23},
            {6:11},
            {6:27},
            {}
        ]
        self.g = EdgeWeightedGraph(7)
        for i, adj in enumerate(vertices):
            for j, weight in adj.items():
                self.g.add_edge(Edge(i, j, weight))
        self.mst = KruskalMST(self.g)

    def test_num_edges_graph(self):
        self.assertEqual( len(list(self.g.edges())), 12 )

    def test_num_edges_mst(self):
        self.assertEqual( len(list(self.mst.edges())), 6 )

    def test_mst_weight(self):
        total_weight = 0
        for e in self.mst.edges():
            total_weight += e.get_weight()
        self.assertEqual( total_weight, 93 )


if __name__ == '__main__':
    unittest.main()
