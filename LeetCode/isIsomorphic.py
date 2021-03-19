#!/bin/python
#See: https://leetcode.com/problems/isomorphic-strings/
import sys
import string
from collections import Counter
# Complete the twoStrings function below.
def isIsomorphic(s, t):

    diff = dict()

    for i in range(0,len(s)):
        if (s[i] not in diff.keys()):
            if (t[i] in diff.values()):
                return False
            diff[s[i]] = t[i]
        else:
            if (diff[s[i]] != t[i]):
                return False

    return True
if __name__ == '__main__':
        s = raw_input()

        t = raw_input()

        result = isIsomorphic(s, t)

        print(result)
