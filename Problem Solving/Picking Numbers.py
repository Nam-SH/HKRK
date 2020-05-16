def pickingNumbers(s):

    s = sorted(s)
    res = []
    for i in range(n-1):
        sub = [s[i]]
        for j in range(i+1, n):
            if abs(s[i] - s[j]) <= 1:
                sub.append(s[j])
        res.append(sub)

    MAX = len(res[0])
    for i in res:
        if MAX < len(i):
            MAX = len(i)

    return MAX


n = int(input().strip())
s = list(map(int, input().rstrip().split()))
pickingNumbers(s)


# def pickingNumbers(s):

#     MAX = 0
#     for i in s:
#         b = s.count(i)
#         c = s.count(i-1)
#         d = b + c
#         if MAX < d:
#             MAX = d

#     return MAX


# n = int(input().strip())
# s = list(map(int, input().rstrip().split()))
# pickingNumbers(s)
