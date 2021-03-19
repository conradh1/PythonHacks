#!/bin/python

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/flipping-bits/problem

# Complete the flippingBits function below.
def flippingBits(n):
    a = list('{:032b}'.format(n))
    b = ''

    for i in range(0,len(a)):
        if (a[i] == '1'):
            b += '0'
        else:
            b += '1'
    return(int(b, 2))


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        n = int(raw_input())

        result = flippingBits(n)
        print result

        #fptr.write(str(result) + '\n')

    #fptr.close()
