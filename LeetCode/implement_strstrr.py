#!/bin/python
#See: https://leetcode.com/problems/implement-strstr/
import sys
import string
from collections import Counter
# Complete the twoStrings function below.
def strStrslow(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """        
    n = -1    

    if (not haystack and not needle):
        return 0

    for i in range(0,len(haystack)):
        x = i
        y = 0
        while ( x < len(haystack) and y < len(needle) and haystack[x] == needle[y]):
            x += 1
            y += 1
        if ( y == len(needle)):
            n = i
            return n
                 
    return n


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """ 

    if (not haystack and not needle):
        return 0
    return haystack.find(needle)

if __name__ == '__main__':
        h = raw_input()
        n = raw_input()

        print(str(strStr(h, n)))        
