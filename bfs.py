from collections import deque


def bfs(G, source):
    """Modifies vertices within graph G without returning
    anything."""
    for v in G:
        v.dist = float("inf")
        v.prev = None
    source.dist = 0

    q = deque([source])
    while len(q):
        u = q.popleft()
        for v in u.get_neighbors():
            if v.dist == float("inf"):
                v.dist = u.dist + 1
                v.prev = u
                q.append(v)
