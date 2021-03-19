#!/usr/bin/python

#Python use of set combinations example
#See: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
import sys
import string
from itertools import combinations_with_replacement

if __name__ == '__main__':
    myInput = raw_input().split() #input for string and number of combinations.
    setA = list(myInput[0]) 
    n = len(myInput[0]) #case no second argument
        
    if (len(myInput) == 2): 
        n = int(myInput[1])    
    
    CR = list(combinations_with_replacement(sorted(setA),n))
    
    for i in range(len(CR)):
            print ''.join(CR[i])