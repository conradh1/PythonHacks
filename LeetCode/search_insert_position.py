#!/bin/python
#https://leetcode.com/problems/search-insert-position/

import math
import os
import random
import re
import sys


def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        x= 0
        found = False
        if (target > nums[len(nums)-1]):
            x= len(nums)        
        while (i < len(nums) and not found ):
            n = nums[i]
            if (n >= target):
                x = i
                found = True     
            i += 1
        
        return x 
        
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().rstrip().split())

    res = searchInsert(arr,n)
    print (str(res))
    
