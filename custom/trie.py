class Node(object):
    def __init__(self, R=256, value=None):
        self.R = R
        self.value = value
        self.next = [None] * self.R

class RWT(object):
    def __init__(self):
        self.root = Node()

    def put(self, s, value):
        node = self.root
        for char in s:
            index = ord(char)
            if node.next[index] is None:
                node.next[index] = Node()
            node = node.next[index]
        node.value = value

    def get(self, s):
        node = self.root
        for char in s:
            node = node.next[ord(char)]
            if node is None:
                return None
        return node.value

    def contains(self, s):
        return self.get(s) is not None

    def delete(self, s):
        self._delete(s, 0, None, self.root)

    def _delete(self, s, d, prev, node):
        prev, node = node, node.next[ord(s[d])]
        if node is None:
            return
        if d == len(s) - 1:
            node.value = None
        else:
            self._delete(s, d+1, prev, node)
        if len(set(node.next)) == 1:
            prev.next[ord(s[d])] = None



if __name__ == '__main__':
    rwt = RWT()
    rwt.put('sally', 5)
    rwt.put('sells', 9)
    rwt.put('sea', 3)
    rwt.put('sitting', 4)
    rwt.put('by', 1)
    rwt.put('the', 2)
    rwt.put('sea', 8)
    rwt.put('shells', 7)
    rwt.put('shore', 3)
    rwt.put('she', 11)

    print(rwt.get("shells"))
    print(rwt.get("shore"))
    print(rwt.get("shelter"))
    print(rwt.get("she"))
    print(rwt.get("by"))
    print(rwt.get("dog"))

    print()
    print(rwt.contains("cat"))
    print(rwt.contains("sea"))

    print()
    rwt.delete("shore")
    print(rwt.get("shore"))
    print(rwt.get("she"))
    rwt.delete("she")
    print(rwt.get("she"))
    print(rwt.get("shells"))
    rwt.delete("shells")
    rwt.delete("shells")
    print(rwt.get("shells"))








