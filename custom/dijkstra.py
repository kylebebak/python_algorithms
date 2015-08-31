# from custom.heapdict import heapdict
from .heapdict import heapdict

def dijkstra(gr, source):
    """Returns dict of (vertex -> dist) pairs and dict
    of (vertex -> previous_vertex) pairs."""
    dist = {}
    prev = {}

    dist[source] = 0
    q = heapdict()

    for v in gr:
        if v != source:
            dist[v] = float("inf")
            prev[v] = None
        q[v] = dist[v]

    while len(q):
        u = q.popitem()[0]
        for v in u.get_neighbors():
            alt = dist[u] + u.get_weight(v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                q[v] = alt

    return {'dist': dist, 'prev': prev}


