import random


def shuffle(l):
    for i in range(len(l), 1, -1):
        r = random.randrange(i)
        l[r], l[i - 1] = l[i - 1], l[r]
    return l
