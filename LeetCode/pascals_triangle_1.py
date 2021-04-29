#!/bin/python
#hhttps://leetcode.com/problems/pascals-triangle/

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        row = []
        pas = []
        
        row.append(1)
        pas.append(row)
        
        if (numRows == 1):
            return pas
        
        r = 1
        row = []
        
        while (r < numRows):
            row.append(1)            
            for i in range(1,r):                
                row.append(pas[r-1][i-1]+pas[r-1][i])
            row.append(1)
            pas.append(row)
            row = []
            r += 1
        return pas

if __name__ == '__main__':
    n = int(raw_input().rstrip())
    print (str(generate(n)))
    
