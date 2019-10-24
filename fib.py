def fib(N):
    """
    >>> fib(10)
    55
    >>> fib(100)
    354224848179261915075

    >>> fib(0)
    Traceback (most recent call last):
        ...
    TypeError: Only accepts positive integers.

    >>> fib(20.5)
    Traceback (most recent call last):
        ...
    TypeError: Only accepts positive integers.
    """

    if not isinstance(N, int) or N <= 0:
        raise TypeError("Only accepts positive integers.")

    n0, n1 = 0, 1
    for i in range(1, N):
        n0, n1 = n1, n0 + n1
    return n1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
