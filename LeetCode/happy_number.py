#!/bin/python
#See: https://leetcode.com/problems/length-of-last-word/
import sys
import string
import re
#https://leetcode.com/problems/happy-number/submissions/

def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if (n == 1):
        return True
    
    happy = str(n)
    dups = []
    t = 0
    
    while ( 1 ==1):   
        for i in range(0,len(happy)):                
            t += pow(int(happy[i]),2)            
        happy = str(t)            
        if ( t == 1):
            return True
        else:
            if (t in dups):
                return False                
            dups.append(t)
            t = 0
if __name__ == '__main__':
        i = int(raw_input().rstrip())
        print(str(isHappy(w)))            