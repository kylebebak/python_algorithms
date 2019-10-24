from collections import deque


def dfs(G, source):
    """Modifies vertices within graph G without returning
    anything."""
    for v in G:
        v.marked = False
        v.prev = None
    source.marked = True

    q = deque([source])
    while len(q):
        u = q.pop()
        for v in u.get_neighbors():
            if not v.marked:
                v.marked = True
                v.prev = u
                q.append(v)
