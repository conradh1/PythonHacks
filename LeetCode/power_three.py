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
    isThree = False

    if num < 0 or num == 2: return False
    count = 0
    three = 3

    if (num == pow(3, count) ):
        isThree = True
    else:
        count += 1

    while (three <= num):
        three = pow(3,count)
        if (three  == num):
            isThree = True
            break
        else:
            count += 1

    return isThree
if __name__ == '__main__':
    num = int(raw_input().rstrip())

    print(powerTwo(num))
