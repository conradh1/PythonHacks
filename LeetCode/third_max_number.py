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
    
    if (len(nums) == 1):
        return nums[0]
    elif(len(nums) == 2):
        if (nums[0] > nums[1]):
            return nums[0]
        else:
            return nums[1]    
    else:
        top = nums[0]
        middle = nums[1]
        bottom = nums[2]
        
        for i in range(0,len(nums)):
            x = nums[i]
            if ( x > top):
                if (top > middle):
                    bottom = middle
                    middle = top
                elif (top < middle and top > bottom):
                    bottom = top
                elif ( top < bottom):
                    bottom = top
                top = x
            elif (x < top and x > middle):
                if ( middle > bottom):
                    bottom = middle                
                middle = x
            elif (x < top and x < middle and x > bottom):
                bottom = x                
                
        return bottom

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    res = thirdMax(arr)
    print (str(res))
    
