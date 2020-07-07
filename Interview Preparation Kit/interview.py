#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy


def checkWords(crossword, k, i, j, direct):

    if k == len(words):
        return answer.append(crossword)

    if words[k] == ';':
        return findEmpty(crossword, k + 1)

    if not (0 <= i < 10 > j >= 0) or crossword[i][j] == "+":
        return

    if crossword[i][j] != '-' and crossword[i][j] != words[k]:
        return

    copy_crossword = deepcopy(crossword)
    copy_crossword[i][j] = words[k]

    if direct == 1:
        checkWords(copy_crossword, k + 1, i, j + 1, 1)
    elif direct == 2:
        checkWords(copy_crossword, k + 1, i + 1, j, 2)


def findEmpty(crossword, k):
    for i in range(10):
        for j in range(10):
            if crossword[i][j] != '+':
                checkWords(crossword, k, i, j, 1)
                checkWords(crossword, k, i, j, 2)


def crosswordPuzzle(crossword, words):
    global answer

    crossword = [list(s) for s in crossword]

    answer = []
    findEmpty(crossword, 0)
    return ["".join(s) for s in answer[0]]


crossword = [
    "XXXXXX-XXX",
    "XX------XX",
    "XXXXXX-XXX",
    "XXXXXX-XXX",
    "XXX------X",
    "XXXXXX-X-X",
    "XXXXXX-X-X",
    "XXXXXXXX-X",
    "XXXXXXXX-X",
    "XXXXXXXX-X",
]

words = "ALMATY;PANAMA;ICELAND;MEXICO"

result = crosswordPuzzle(crossword, words)
print(('\n'.join(result)))
