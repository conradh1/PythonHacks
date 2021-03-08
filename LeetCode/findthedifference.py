#!/bin/python
#See: https://leetcode.com/problems/find-the-difference/
import sys
import string
from collections import Counter
# Complete the twoStrings function below.
def findTheDifference(s, t):
    s_total = 0
    t_total = 0

    for i in range(0,len(s)):
        s_total += ord(s[i])
        t_total += ord(t[i])

    t_total += ord(t[len(t)-1])
    diff = chr(t_total-s_total)

    return diff

if __name__ == '__main__':
        s = raw_input()

        t = raw_input()

        result = findTheDifference(s, t)

        print(result)
