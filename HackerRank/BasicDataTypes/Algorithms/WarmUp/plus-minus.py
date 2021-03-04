#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0;
    neg = 0;
    zero = 0;
    bottom = float(len(arr))

    for i in range(0,len(arr)):
        if ( arr[i] > 0):
            pos += 1
        elif ( arr[i] < 0):
            neg += 1
        else:
            zero += 1

    neg = float(neg / bottom)
    pos = float(pos / bottom)
    zero = float(zero / bottom)
    print('%.6f' %pos)
    print('%.6f' %neg)
    print('%.6f' %zero)

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)
