#!/bin/python
#https://leetcode.com/problems/add-binary/

import math
import os
import re
import sys

# Complete the minimumSwaps function below.
def add_binary(a,b):

    top = max(len(a), len(b))
    bin = ''
    carry = '0'

    # make arrays the same length
    if ( top > len(a)):
        for i in range(0,top - len(a)):
            a = '0'+a
    elif ( top > len(b)):
        for i in range(0,top - len(b)):
            b = '0'+b
    
    # add the arrays.
    for i in range(top-1,-1,-1):
        if (a[i] == '1' and b[i] == '1'):            
            if ( carry == '0'):                
                bin = '0'+bin
                carry = '1'
            else:
                bin = '1'+bin
        elif (a[i] == '1' or b[i] == '1'):
            if ( carry == '0'):
                bin = '1'+bin
            else:
                bin = '0'+bin
        else:   
            if ( carry == '0'):         
                bin = '0'+bin
            else:
                bin = '1'+bin
                carry = '0'
    

    # last bit to check
    if (carry == '1'):
        bin = '1'+bin

    return bin



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = str(raw_input())
    b = str(raw_input())

    print (str(add_binary(a,b)))
    