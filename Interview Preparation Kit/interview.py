def poisonousPlants(p):

    temp = []
    Max = 0

    for i in p:
        days = 1
        while temp and temp[-1][0] >= i:
            val, d = temp.pop()
            days = max(days, d + 1)

        if not temp:
            days = 0

        Max = max(Max, days)
        temp.append((i, days))

    return Max


n = 7
poisonousPlants([6, 5, 8, 4, 7, 10, 9])
