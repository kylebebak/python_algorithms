
def countingsort(a):
    k = max(a) + 1
    count = [0] * k

    for key in a:
        count[key] += 1

    sum = 0
    for i in range(k):
        old_count = count[i]
        count[i] = sum
        sum += old_count

    aux = [None] * len(a)
    for key in a:
        aux[count[key]] = key
        count[key] += 1

    return aux
