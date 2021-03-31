#!/bin/python
# https://www.hackerrank.com/challenges/picking-numbers/problem

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    
    top = 0
    for i in a:
        c=a.count(i)
        d=a.count(i-1)
        c=c+d
        if c > top:
            top=c
    return(top)


    

if __name__ == '__main__':
    

    n = int(raw_input().strip())
    a = map(int, raw_input().rstrip().split())
    result = pickingNumbers(a)
    print(str(result))


