#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the roadsAndLibraries function below.
def dfs(arr, idx, visit):
    
    if visit[idx]:
        return 0

    visit[idx] = 1
    cnt = 1

    for v in arr[idx]:
        cnt += dfs(arr, v, visit)
    return cnt


def roadsAndLibraries(n, c_lib, c_road, cities):

    arr = [[] for _ in range(n + 1)]
    visit = [0] * (n + 1)

    for u, v in cities:
        arr[u] += [v]
        arr[v] += [u]

    cost = 0
    for i in range(1, n + 1):
        cnt = dfs(arr, i, visit)
        if cnt:
            cost += c_lib + (cnt - 1) * min(c_lib, c_road)
    return cost


q = 1
for q_itr in range(q):
    n = 3

    m = 3

    c_lib = 2

    c_road = 1

    cities = [[1, 2], [3, 1], [2, 3]]

    result = roadsAndLibraries(n, c_lib, c_road, cities)

    print(result)