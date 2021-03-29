#!/bin/python
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):    
    count = [0,0]

    if (len(scores) <= 1):
        return count
    # assign first index
    low = scores[0]
    high = scores[0]

    for i in range(1,len(scores)):
        # check max
        if (scores[i] > high):
            count[0] += 1
            high = scores[i]
        elif (scores[i] < low):
            count[1] += 1
            low = scores[i]

    return count
if __name__ == '__main__':
    n = int(raw_input())

    scores = map(int, raw_input().rstrip().split())
    result = breakingRecords(scores)

    print(' '.join(map(str, result)))    
