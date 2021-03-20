#!/bin/python

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(arr, d):
    d = d%len(arr)
    print d
    print arr[d:]
    print arr[:d]
    arr = arr[d:]+arr[:d]
    return arr



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    print(' '.join(map(str, result)))    
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
