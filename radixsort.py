"""
For sorting integers with values >= 0. The second method benefits
from a cleaner implementation by assigning one extra spot in the
count array.
"""


def radix_i0(a):
    R = max(a) + 1
    count = [0] * R

    for key in a:
        count[key] += 1

    sum = 0
    for i in range(R):
        old_count = count[i]
        count[i] = sum
        sum += old_count

    aux = [None] * len(a)
    for key in a:
        aux[count[key]] = key
        count[key] += 1

    return aux


def radix(a, R=None):
    R = max(a) + 2 if R is None else R
    count = [0] * R

    for key in a:
        count[key + 1] += 1

    for i in range(R - 1):
        count[i + 1] += count[i]

    aux = [None] * len(a)
    for key in a:
        aux[count[key]] = key
        count[key] += 1

    return aux


def lsd_radix(a):
    """
    Sorts an array of strings by performing a radix sort
    on each letter, starting with the least significant
    (rightmost) letter and moving to the left.
    """


if __name__ == "__main__":
    import random

    l = [random.randrange(100) for i in range(1000)]
    print(radix_i0(l))

    l = [random.randrange(100) for i in range(1000)]
    print(radix(l))
