def maximumSum(a=[3, 3, -9, 9, 5], m=7):

    n = 5

    sub = []
    curr = 0
    for i in range(n):
        curr = (a[i] + curr) % m
        sub += [curr]

    Max = max(sub)
    sub = sorted([(j, i) for (i, j) in enumerate(sub)])

    for i in range(n):
        if sub[i - 1][1] > sub[i][1] and sub[i - 1][0] < sub[i][0]:
            Max = max(Max, (sub[i][0] - sub[i - 1][0]) % m)

    print(Max)
    return (Max)



maximumSum()
