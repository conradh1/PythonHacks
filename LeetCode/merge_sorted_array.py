
#!/bin/python
#https://leetcode.com/problems/merge-sorted-array/

import math
import os
import random
import re
import sys

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int index to march down nums1
    :type nums2: List[int]
    :type n: int length of nums2
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    i,j=0,0    

    while (i < m and j < n):
        if (nums1[i] > nums2[j]):
            for x in range(m,i,-1):
                nums1[x] = nums1[x-1]            
            nums1[i] = nums2[j]
            m += 1            
            j += 1
        i += 1

    while (j < n):
        nums1[m] = nums2[j]
        j +=1
        m += 1

    print(nums1)

        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #a = map(int, raw_input().rstrip().split())
    #b = map(int, raw_input().rstrip().split())
    a = [1,2,3,0,0,0]
    m = 3
    b = [2,5,6]
    n = 3

    merge(a, len(a)-len(b), b, len(b)) 
    #fptr.write(str(res) + '\n')

    #fptr.close()
