
#!/bin/python
#https://leetcode.com/problems/contains-duplicate-ii/submissions/

import math
import numpy as np
import random
import re
import sys

def mines(n,m,k):
        """
        n,m dimensions
        k - number of mines
        """
        field = np.zeros((n,m))

        i = 0
        while (i < k):
            x = random.randint(0,n-1)
            y = random.randint(0,m-1)
            if (field[x][y] == 0):
                field[x][y] = 1
                i += 1
        for i in range(0,len(field)):
            print('[', end ='')
            for j in range(0, len(field[i])):
                print(str(field[i][j]), end=',')
            print(']')
        
if __name__ == '__main__':
           
    mines(6,6,6)
    
