#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxXor function below.
def maxXor(arr, queries):
    ans = []
    trie = [[0, 0]]
    k = len(bin(max(arr + queries))) - 2

    print(['{:b}'.format(x) for x in arr])
    for number in ['{:b}'.format(x).zfill(k) for x in arr]:
        node = trie[0]
        for ch in number:
            if node[int(ch)] == 0:
                trie.append([0, 0])
                node[int(ch)] = len(trie) - 1
            node = trie[node[int(ch)]]
    for n in queries:
        node = trie[0]
        res = ''
        for ch in '{:b}'.format(n).zfill(k):
            neg = int(ch) ^ 1
            if node[neg] == 0:
                neg = int(ch)
            res += str(neg)
            node = trie[node[neg]]
        ans.append(int(res, 2) ^ n)
    return ans


n = 4

arr = [1, 3, 5, 7]

m = 2
queries = [17, 6]

result = maxXor(arr, queries)

print(result)
