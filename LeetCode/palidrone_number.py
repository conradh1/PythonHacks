#!/bin/python
#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

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
    print(s.lower())    
