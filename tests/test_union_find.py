import unittest
from custom.union_find import UF


class TestUF(unittest.TestCase):
    def setUp(self):
        self.uf = UF(10)
        self.uf.union(0, 1)
        self.uf.union(1, 2)
        self.uf.union(2, 4)
        self.uf.union(9, 0)

        self.uf.union(3, 5)
        self.uf.union(6, 5)
        self.uf.union(7, 5)
        self.uf.union(3, 8)

    def test_conn_1(self):
        self.assertEqual(self.uf.connected(2, 9), True)

    def test_conn_2(self):
        self.assertEqual(self.uf.connected(8, 7), True)

    def test_before_connecting(self):
        self.assertEqual(self.uf.connected(5, 1), False)

    def test_after_conntecting(self):
        self.uf.union(8, 0)
        self.assertEqual(self.uf.connected(5, 1), True)


if __name__ == "__main__":
    unittest.main()
