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

    if (num == 1):
        return True
    if (num < 3):
        return False

    t = num

    while (t % 3 == 0):
        if (t == 3):
            return True
        t = t/3


    return isThree
if __name__ == '__main__':
    num = int(raw_input().rstrip())

    print(powerTwo(num))
