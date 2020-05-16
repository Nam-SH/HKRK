import sys
import re
import random
import os
import math


def formingMagicSquare(s):

    all_p = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    diffs = []
    for p in all_p:
        cost = 0
        for i, j in list(zip(s, p)):
            for ii, jj in (list(zip(i, j))):
                if ii != jj:
                    cost += abs(ii - jj)
        diffs.append(cost)

    return min(diffs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = [list(map(int, input().rstrip().split())) for _ in range(3)]

    result = formingMagicSquare(s)
    fptr.write(str(result) + '\n')
    fptr.close()
