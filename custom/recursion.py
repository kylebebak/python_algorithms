def flatten(a):
    """
    >>> flatten([ [1, 2, [3, 4] ], [5, 6], 7])
    [1, 2, 3, 4, 5, 6, 7]
    """
    result = []

    for x in a:
        if isinstance(x, list):
            result += flatten(x)
        else:
            result.append(x)
    return result


def flatten_dict(d, prefix='', result={}):
    """
    >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3, 'z': {'t': 5, 'u': 6}}, 'c': 4})
    {'a': 1, 'b.x': 2, 'b.y': 3, 'b.z.t': 5, 'b.z.u': 6, 'c': 4}
    """
    for key, value in d.items():
        if isinstance(value, dict):
            flatten_dict(value, prefix + key + '.' , result)
        else:
            result[prefix + key] = value
    return result


def unflatten_dict(dictionary, separator='.'):
    """
    Uses iteration rather than recursion, and makes use of pointers
    to build up the result dict from each key-value pair of the input
    dictionary.

    >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'b.z.t': 5, 'b.z.u': 6})
    {'a': 1, 'b': {'x': 2, 'y': 3, 'z': {'t': 5, 'u': 6}}}

    >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
    {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
    """
    result = dict()

    for key, value in dictionary.items():
        parts = key.split(separator)
        d = result
        for part in parts[:-1]:
            if part not in d:
                d[part] = dict()
            d = d[part]
        d[parts[-1]] = value
    return result


list(map(lambda x: x*x, [1, 2, 3, 4, 5]))


def tree_map(func, l, flat=False):
    """
    >>> tree_map(lambda x: x*x, [1, 2, [3, 4, [5]]], flat=True)
    [1, 4, 9, 16, 25]
    >>> tree_map(lambda x: x*x, [1, 2, [3, 4, [5]]])
    [1, 4, [9, 16, [25]]]
    """
    result = []

    for x in l:
        if isinstance(x, list):
            if flat:
                result += tree_map(func, x, flat)
            else:
                result += [tree_map(func, x, flat)]
        else:
            result.append(func(x))

    return result


def tree_reverse(l, flat=False):
    """
    >>> tree_reverse([[1, 2], [3, [4, 5]], 6])
    [6, [[5, 4], 3], [2, 1]]
    """
    result = []

    for x in l[::-1]:
        if isinstance(x, list):
            if flat:
                result += tree_reverse(x, flat)
            else:
                result += [tree_reverse(x, flat)]
        else:
            result.append(x)

    return result


def permute(l):
    """
    >>> permute([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    perm_list = []
    if len(l) <= 1:
        return l

    for k in range(len(l)):
        permutations = permute(l[:k] + l[(k + 1):])
        for perm in permutations:
            if not isinstance(perm, list):
                perm_list.append([l[k]] + [perm])
            else:
                perm_list.append([l[k]] + perm)

    return perm_list


def fib(N):
    if not isinstance(N, int) or N <= 0:
        raise TypeError("Only accepts positive integers.")

    n0, n1 = 0, 1
    for i in range(1, N):
        n0, n1 = n1, n0+n1
    return n1




