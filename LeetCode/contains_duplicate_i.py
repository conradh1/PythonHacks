
#!/bin/python
#https://leetcode.com/problems/contains-duplicate-ii/submissions/

import math
import os
import random
import re
import sys

def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i in range(0, len(nums)):
            x = nums[i]
            if (x in d):
                if (abs(d[x] - i) <= k):
                    return True
                else:
                    d[x] = i
            else:
                d[x] = i
        return False
        
if __name__ == '__main__':
    
    #a = map(int, raw_input().rstrip().split())
    #b = map(int, raw_input().rstrip().split())
    a = [1,2,3,1,2,3]
    k = 2  

    print str(containsNearbyDuplicate(a, k))
    a = [1,2,3,1]
    k = 3
    print str(containsNearbyDuplicate(a, k))
    
