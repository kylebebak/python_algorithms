class Node(object):
    def __init__(self, char, value=None):
        self.char = char
        self.value = value
        self.left, self.middle, self.right = None, None, None

class TST(object):
    def __init__(self):
        self.root = None

    def put(self, s, value):
        self.root = self._put(self.root, s, value, 0)

    def _put(self, node, s, value, d):
        char = s[d]
        if node is None:
            node = Node(char)
        if char < node.char:
            node.left = self._put(node.left, s, value, d)
        elif char > node.char:
            node.right = self._put(node.right, s, value, d)
        # char is equal to char at node
        elif d < len(s)-1:
            node.middle = self._put(node.middle, s, value, d+1)
        else:
            node.value = value
        return node

    def get(self, s):
        node = self._get(self.root, s, 0)
        if node is None:
            return None
        return node.value

    def _get(self, node, s, d):
        if node is None:
            return None
        char = s[d]
        if char < node.char:
            return self._get(node.left, s, d)
        elif char > node.char:
            return self._get(node.right, s, d)
        # char is equal to char at node
        elif d < len(s)-1:
            return self._get(node.middle, s, d+1)
        else:
            return node

    def contains(self, s):
        return self.get(s) is not None



if __name__ == '__main__':
    tst = TST()

    tst.put('sally', 5)
    tst.put('sells', 9)
    tst.put('sea', 3)
    tst.put('sitting', 4)
    tst.put('by', 1)
    tst.put('the', 2)
    tst.put('sea', 8)
    tst.put('shells', 7)
    tst.put('shore', 3)
    tst.put('she', 11)

    print("sally", tst.get("sally"))
    print("sea", tst.get("sea"))
    print("shells", tst.get("shells"))
    print("shore", tst.get("shore"))
    print("shelter", tst.get("shelter"))
    print("she", tst.get("she"))
    print("by", tst.get("by"))
    print("dog", tst.get("dog"))

    print()
    print(tst.contains("cat"))
    print(tst.contains("sea"))


