import math

def sieve(n=1):
    """This function accepts an integer n > 1, and returns an ascending list
    of all primes less than or equal to n.
    """
    assert type(n) is int and n > 1, "n must be an integer greater than 1, you passed {0}".format(n)
    primes = [True] * (n+1)

    # invalidate non-primes
    i, limit = [2, int(math.sqrt(n))]
    while i <= limit:
        if primes[i]:
            prime = i*i
            while prime <= n:
                primes[prime] = False
                prime += i
        i += 1

    # populate list of primes and return list
    p = []
    for prime, check in enumerate(primes):
        if prime > 1 and check:
            p.append(prime)
    return (p)
