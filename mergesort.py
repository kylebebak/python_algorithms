def mergesort(a):
    def merge(a, aux, lo, mid, hi):
        """
        Stably merge a[lo..mid] with a[mid+1..hi] using aux[lo..hi].
        """
        # copy to aux[]
        for k in range(lo, hi + 1):
            aux[k] = a[k]

        # merge back to a[]
        i, j = lo, mid + 1
        for k in range(lo, hi + 1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1

    def sort(a):
        """
        Rearranges the array in ascending order.
        """
        N = len(a)
        aux = [0] * N
        n = 1
        while n < N:
            i = 0
            while i < N - n:
                lo = i
                m = i + n - 1
                hi = min(i + n + n - 1, N - 1)
                merge(a, aux, lo, m, hi)
                i += n + n
            n = n + n

    sort(a)
    return a


if __name__ == "__main__":
    a = mergesort([4, 1, 3, 2])
    print(a)
