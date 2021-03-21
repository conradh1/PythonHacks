#!/bin/python
#See: https://leetcode.com/problems/length-of-last-word/
import sys
import string
import re
from collections import Counter


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.rstrip()    
    words = s.split(' ')
    last = words[len(words)-1]
    return len(last)

if __name__ == '__main__':
        w = raw_input()
        

        print(str(lengthOfLastWord(w)))        
