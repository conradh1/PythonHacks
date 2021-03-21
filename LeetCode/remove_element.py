#!/bin/python
#See: https://leetcode.com/problems/remove-element/
import sys
import string

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    top = len(nums)
    i = 0
    
    while (i < top):
        if nums[i] == val:
            nums.pop(i)
            top = len(nums)
        else:
            i += 1
    #print (str(nums))    
    return (len(nums))


if __name__ == '__main__':
        arr = map(int, raw_input().rstrip().split())
        n = int(raw_input().rstrip())
        print(str(removeElement(arr, n)))        
