class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def get_root(self):
        return self.root.value

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            self.size += 1
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
                self.size += 1
        elif value > node.value:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)
                self.size += 1

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node.value
        elif value < node.value and node.left is not None:
            return self._find(value, node.left)
        elif value > node.value and node.right is not None:
            return self._find(value, node.right)

    def delete_tree(self):
        # garbage collector will take care of this
        self.root = None

    def print(self):
        if self.root is not None:
            self._print(self.root)

    def _print(self, node):
        if node is not None:
            self._print(node.left)
            print(str(node.value) + ' ')
            self._print(node.right)

    def basic_dfs(self):
        for node_value in self._basic_dfs(self.root):
            yield node_value

    def _basic_dfs(self, node):
        if node is not None:
            yield node.value
            for node_value in self._basic_dfs(node.left):
                yield node_value
            for node_value in self._basic_dfs(node.right):
                yield node_value




def basic_dfs(node):
    if node is not None:
        yield node.value
        for node_value in basic_dfs(node.left):
            yield node_value
        for node_value in basic_dfs(node.right):
            yield node_value


if __name__ == '__main__':
    import bst
    import random

    t = bst.BST()

    for i in range(25):
        t.add(random.randrange(100))

    for e in t.basic_dfs():
        print(e)






