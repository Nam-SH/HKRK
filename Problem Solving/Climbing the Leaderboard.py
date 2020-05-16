import math
import os
import random
import re
import sys


def climbingLeaderboard(scores, alice):
    scores = list(sorted(set(scores), reverse=True))
    a = len(alice) - 1
    s = 0

    res = []
    while a >= 0:
        if s == len(scores) or scores[s] <= alice[a]:
            res.append(s + 1)
            a -= 1
        else:
            s += 1

    return reversed(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
