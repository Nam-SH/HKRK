#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minTime function below.
# def minTime(roads, machines):
#     arr = [[] for _ in range(n)]
#     for i, j, k in roads:
#         arr[i] += [(j, k)]
#         arr[j] += [(i, k)]
#
#     visit = [0] * n
#     ans = []
#     for val in machines:
#         for nxt, weight in arr[val]:
#             if visit[nxt]: continue
#             visit[nxt] = 1
#             ans += [weight]
#     ans.sort()
#     return sum(ans[:2])


n = 10
k = 10

# roads = [[2, 1, 8], [1, 0, 5], [2, 4, 5], [1, 3, 4]]
# machines = [2, 4, 0]

roads = [
    [4, 6, 4],
    [6, 5, 4],
    [6, 1, 9],
    [5, 2, 5],
    [6, 7, 4],
    [1, 8, 3],
    [6, 0, 9],
    [8, 9, 10],
    [5, 3, 7]
]
machines = [1, 2, 4, 9, 0, 7, 5, 3, 6, 8]

result = minTime(roads, machines)

print(result)
