#!/bin/python
#See: https://leetcode.com/problems/rotate-array/
import sys
import string


def rotatebetter(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0   
    c = 0                     
    t1 = nums[i]
    while ( c < len(nums)):          
        if ((i + k) < len(nums)):
            t2 = nums[i+k]
            nums[i+k] = t1            
            i += k
            t1 = t2
        else:
            nums[len(nums)-(i+k)] = t1
            i += 1   
            t1 = nums[i]     
        c += 1
        
        
    print nums

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0                    
    while ( i < k):
        t1 = nums[0]
        for j in range(0,len(nums)-1):
            t2 = nums[j+1]
            nums[j+1] = t1
            t1 = t2            
        nums[0] = t1
        i += 1
    print nums

if __name__ == '__main__':
        #arr = map(int, raw_input().rstrip().split())
        #n = int(raw_input().rstrip())
        nums = [1,2,3,4]
        k = 2
        rotatebetter(nums,k)
        
