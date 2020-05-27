def getMinimumCost(k=3, c=[1, 3, 5, 7, 9]):

    c.sort(reverse=True)

    res = 0
    for i in range(n):
        print(c[i] * (i // k + 1))
        res += c[i] * (i // k + 1)

    return res

getMinimumCost()