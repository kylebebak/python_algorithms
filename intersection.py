import random

def intersection(a, b):
    """Returns index at which element e is found in
    list l. List l must be sorted, or else binary search
    will fail. If e not in l, binary search returns -1."""
    sa = set()
    intersect = set()
    for e in a:
        sa.add(e)
    for e in b:
        if e in sa:
            intersect.add(e)
    return intersect



if __name__ == '__main__':
    a = [random.randrange(100) for i in range(25)]
    b = [random.randrange(100) for i in range(25)]
    print(sorted(a))
    print(sorted(b))
    print(intersection(a, b))
