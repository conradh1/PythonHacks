#!/bin/python
#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps= 0
    tmp = 0
    i = 0
    while (i < len(arr)):
        if ( arr[i] == (i+1)):
            i += 1
        else:
            for j in range(i+1,len(arr)):
                if ((j+1) == arr[i]):
                    swaps += 1
                    tmp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = tmp
                    break
    return swaps

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)
    print (str(res))
    #fptr.write(str(res) + '\n')

    #fptr.close()
