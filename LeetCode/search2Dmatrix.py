
#!/bin/python
#See: https://leetcode.com/problems/search-a-2d-matrix/
import sys
import string
from collections import Counter
# Complete the twoStrings function below.
def searchMatrix(matrix, target):

    # start at the middle
    x = target

    i = len(matrix)/2
        
    for i in range (0,len(matrix)):        
            if (x >= matrix[i][0] and x <= matrix[i][len(matrix[i])-1]):            
                for j in range(0,len(matrix[i])):                
                    if ( matrix[i][j] == x):
                        return True
                return False        
            
    return False

if __name__ == '__main__':
    target= int(raw_input().rstrip())

    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    matrix1 = [1,2,3,4,5,6,7,8,9]
    matrix2 = [[1],[3]]
    result = searchMatrix(matrix2, target)
    print(result)
