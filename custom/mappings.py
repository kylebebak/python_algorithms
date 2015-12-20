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


def flatten_alternate(a, result=[]):
    """
    >>> flatten_alternate([ [1, 2, [3, 4] ], [5, 6], 7])
    [1, 2, 3, 4, 5, 6, 7]
    """
    for x in a:
        if isinstance(x, list):
            flatten_alternate(x, result)
        else:
            result.append(x)
    return result


def flatten_dict(d, prefix='', result={}):
    """
    >>> import pprint
    >>> pprint.pprint(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3, 'z': {'t': 5, 'u': 6}}, 'c': 4}))
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

    >>> import pprint
    >>> pprint.pprint(unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'b.z.t': 5, 'b.z.u': 6}))
    {'a': 1, 'b': {'x': 2, 'y': 3, 'z': {'t': 5, 'u': 6}}}

    >>> pprint.pprint(unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}))
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()

