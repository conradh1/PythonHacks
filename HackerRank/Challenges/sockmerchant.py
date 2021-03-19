#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/sock-merchant/problem

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    socks = dict()
    pairs = 0
    for i in range(0, len(ar)):
        if (ar[i] in socks.keys()):
            socks[ar[i]] += 1
            if (socks[ar[i]] % 2 == 0):
                pairs += 1
        else:
            socks[ar[i]] = 1
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
