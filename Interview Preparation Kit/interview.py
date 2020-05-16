def countTriplets(arr, r):
    from collections import defaultdict

    m2 = defaultdict(int)
    m3 = defaultdict(int)

    total = 0
    for val in arr:
        if val in m3:
            total += m3[val]
        if val in m2:
            m3[val * r] += m2[val]

        m2[val * r] += 1
    print(m2)
    print(m3)
    return total


arr = "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"

arr = list(map(int, arr.split()))
r = 1

print(countTriplets(arr, r))
