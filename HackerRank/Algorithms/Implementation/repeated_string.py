#!/bin/python
# https://www.hackerrank.com/challenges/repeated-string/problem
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    ehs = s.count('a')
    total_ehs = 0
    if ( ehs == 0):
        total_ehs
    length = n / len(s)
    diff = s.count('a',0,(n%len(s)))

    total_ehs = (length * ehs) + diff
    
    return total_ehs
    
if __name__ == '__main__':
    s = raw_input()
    n = int(raw_input())

    result = repeatedString(s, n)
    print(str(result) + '\n')
