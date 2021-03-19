#!/bin/python

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):

    crr = []
    top = len(brr)

    j = 0
    for i in range(0, len(brr)):
        if (j < len(arr) and arr[j] == brr[i]):            
            j += 1
        else:
            crr.append(brr[i])
    return(crr)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    #m = int(raw_input())

    brr = map(int, raw_input().rstrip().split())

    result = missingNumbers(arr, brr)

    print(' '.join(map(str, result)))
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
