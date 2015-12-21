import random

def binary_search(l, e):
    """Returns index at which element e is found in
    list l. List l must be sorted, or else binary search
    will fail. If e not in l, binary search returns -1."""
    lower = 0
    upper = len(l) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if l[mid] == e:
            return mid
        elif l[mid] > e:
            upper = mid-1
        else:
            lower = mid+1
    return -1


if __name__ == '__main__':
    l = [random.randrange(100) for i in range(100)]
    l = list(set(l))
    l.sort()

    print(l)
    for e in range(100):
        print('el: {0}, index: {1}'.format(e, binary_search(l, e)))
