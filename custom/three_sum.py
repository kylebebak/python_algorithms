import itertools, numpy as np


def three_sum(s):
    """
    Creates a hash table so that pairs from the set
    can be checked against other elements in constant time.
    """
    if not isinstance(s, set):
        s = set(s)
    triples = set()
    for pair in itertools.combinations(s, 2):
        third = -sum(pair)
        if third in s and third not in pair:
            triples.add(
                tuple(sorted(list(pair) + [third]))
            )
    return triples


def three_sum_list(l):
    """
    Sorts elements first so that the three_sum
    comparison can be done in quadratic time.
    """
    triples = set()
    l = sorted(list(l))
    n = len(l)
    for i in range(0, n-2):
        a = l[i]
        start = i+1
        end = n-1
        while (start < end):
            b = l[start]
            c = l[end]
            if np.sign(a) == np.sign(b) == np.sign(c):
                # optimized: avoid remaining all-positive/all-negative triples
                return triples
            if (a+b+c == 0):
                triples.add((a,b,c))
                start += 1
                end -= 1
            elif a+b+c > 0:
                end -= 1
            else:
                start += 1
    return triples



if __name__ == '__main__':
    s = set([i for i in range(-100, 100)])
    print(three_sum(s))

    l = [-1, 0, 1, 2, 2, -1, -4]
    print(three_sum_list(l))

    l = [i for i in range(100)]
    print(three_sum_list(l))


