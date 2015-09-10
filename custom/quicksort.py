"""
Quicksort can and should be done in place, so this is not the most
efficient implementation, but it's very elegant and concise.
"""
from custom.shuffle import shuffle
def quicksort(seq):
    shuffle(seq)
    return _quicksort(seq)

def _quicksort(seq):
    if len(seq) <= 1:
        return seq
    lo, pi, hi = partition(seq)
    return _quicksort(lo) + [pi] + _quicksort(hi)

def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi


if __name__ == '__main__':
    import random

    l = [random.randrange(100) for i in range(100)]
    print(quicksort(l))
