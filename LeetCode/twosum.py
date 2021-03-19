#!/bin/python
#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def twosum(arr,target):
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if (arr[i]+arr[j] == target):
                out = [i,j]
                return out

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = twosum(arr,n)
    print (str(res))
    #fptr.write(str(res) + '\n')

    #fptr.close()
