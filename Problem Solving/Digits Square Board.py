#!/bin/python3

import os
import sys

#
# Complete the squareBoard function below.
#


def squareBoard(board):
    #
    # Write your code here.
    #


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        board = []

        for _ in range(n):
            board.append(list(map(int, input().rstrip().split())))

        result = squareBoard(board)

        fptr.write(result + '\n')

    fptr.close()
