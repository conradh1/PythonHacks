#!/bin/python
#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def add_digits(num):

    digits = num
    sum = num

    while digits > 9:
        sum = 0
        for x in str(digits):
            sum += int(x)
        digits = sum

    return sum




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = str(raw_input().rstrip())

    res = add_digits(n)
    print (str(res))
    #fptr.write(str(res) + '\n')

    #fptr.close()
