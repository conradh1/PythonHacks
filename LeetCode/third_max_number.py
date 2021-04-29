#!/bin/python
#https://leetcode.com/problems/third-maximum-number/

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if (len(nums) <= 2):
        return (max(nums))
    
    top = -sys.maxsize-1
    middle = -sys.maxsize-1
    bottom = -sys.maxsize-1
    bottomFound = False

    for x in nums:
        #case top
        if (x > top):            
            if ( top > middle):
                middle = top
            top = x     
        elif (x < top and x > middle):            
            middle = x
            
    for y in nums:
        if (y < top and y < middle ):
            bottomFound = True
            if ( y > bottom):
                bottom = y                    
        

    print "debug "+str(top)+' '+str(middle)+' '+str(bottom)
    # we haven't found bottom
    if ( bottomFound == False ):        
        return top
    
    return bottom
    
if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    res = thirdMax(arr)
    print (str(res))
    
