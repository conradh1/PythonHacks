#!/bin/python
#See: https://leetcode.com/problems/power-of-two/
import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def powerTwo(num):
    isTwo = False

    if num < 0: return False
    # convert to 32 bit binary in string 0101...
    bin= list(format(num, "b").zfill(32))


    if (bin.count('1') == 1):
        isTwo = True

    return isTwo
if __name__ == '__main__':
    num = int(raw_input().rstrip())

    print(powerTwo(num))
