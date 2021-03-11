#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left =0
    right = 0
    bottom = 0
    top = len(arr)-1
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if (i == j):
                left += arr[i][j]
            if (i == bottom and j == top):
                top -= 1
                bottom += 1
                right += arr[i][j]

    return (abs(left - right))




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    print(diagonalDifference(arr))

    #fptr.write(str(result) + '\n')

    #fptr.close()
