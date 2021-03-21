#!/bin/python
#https://leetcode.com/problems/palindrome-number

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def palidrone_number(n):
    if (n <= 10):
        return False
    x = str(n)
    y = x[::-1]

    if ( x == y):
        return True
    return False
    

if __name__ == '__main__':
    n = int(raw_input())
    s = str(palidrone_number(n));
    print(s.lower)    
