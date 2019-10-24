import random


def insertion_sort(l):
    sl = []
    for e in l:
        for i in range(len(sl)):
            if e <= sl[i]:
                sl.insert(i, e)
                break
        else:
            sl.append(e)
    return sl


def bubble_sort(l):
    def swap(l, i, j):
        temp = l[i]
        l[i] = l[j]
        l[j] = temp

    while True:
        swapped = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                swap(l, i, i + 1)
                swapped = True
        if not swapped:
            break
    return l


if __name__ == "__main__":
    l = [random.randrange(100) for i in range(100)]
    print(l)
    print(insertion_sort(l))
    print(bubble_sort(l))
