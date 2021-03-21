#!/bin/python
#https://leetcode.com/problems/valid-parentheses/

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def isValid(s):
    # case for odd number in string
    if (len(s) % 2 == 1):
        return False
    left = []
    
    for i in range(0,len(s)):
        p = s[i]
        if ( p == '(' or p =='[' or p == '{' ):
            left.append(p)
        elif ( p == ')' or p ==']' or p == '}' ):
            if ( not left):
                return False
            else:
                l = left.pop()
                if (l == '(' and p != ')' ):
                    return False
                elif (l == '[' and p != ']' ):
                    return False
                elif (l == '{' and p != '}' ):
                    return False
    if (left):
        return False

    return True
    

if __name__ == '__main__':
    s = str(raw_input())    
    print(str(isValid(s)))    
