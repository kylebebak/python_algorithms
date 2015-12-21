import sys
import random
import math


def bucketsort(d, n):
    """
    Use n buckets to sort list, by assigning each element to its
    appropriate bucket, sorting the elements in each bucket,
    and then merging buckets together in order.
    """
    mn = min(d)
    mx = max(d)
    if isinstance(d[0], tuple):
        mn = mn[0]
        mx = mx[0]
    bucket_width = (mx-mn) / float(n)
    buckets = []
    for b in range(n):
        buckets.append(list())

    gen = (key for key in d) if isinstance(d[0], tuple) else ((key, key) for key in d)
    for key, value in gen:
        index = math.floor((key-mn) / bucket_width)
        if key == mx:
            index -= 1
        if isinstance(d[0], tuple):
            buckets[index].append((key, value))
        else:
            buckets[index].append(key)

    result = []
    for l in buckets:
        result += sorted(l)

    return result







if __name__ == '__main__':
    n = int(sys.argv[1])
    a = [0] * n
    for i in range(n):
        a[i] = random.randrange(n)

    # print(countingsort(a))

    for i in range(n):
        a[i] = random.randrange(n * n)

    print(bucketsort(a, 1000))






