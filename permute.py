def permute(l):
    """
    >>> permute([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    perm_list = []
    if len(l) <= 1:
        return l

    for k in range(len(l)):
        permutations = permute(l[:k] + l[(k+1):])
        for perm in permutations:
            if not isinstance(perm, list):
                perm_list.append([l[k]] + [perm])
            else:
                perm_list.append([l[k]] + perm)

    return perm_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
