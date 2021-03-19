#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/sum-vs-xor/problem

# Complete the sumXor function below.
def sumXor(n):
    c = 0

    for i in range(0,n-1):

        if ((n+i) == (n | i)):
            c += 1
    return c

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    result = sumXor(n)
    print(str(result))

    #fptr.write(str(result) + '\n')

    #fptr.close()
