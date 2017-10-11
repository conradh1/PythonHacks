#!/usr/bin/python

#Python use of set intersection example
#See: https://www.hackerrank.com/challenges/itertools-permutations/problem
import sys
import string
from itertools import permutations

if __name__ == '__main__':
    myInput = raw_input().split() #input for string and number of permutations.
    setA = list(myInput[0]) 
    n = len(myInput[0]) #case no second argument
        
    if (len(myInput) == 2): 
        n = int(myInput[1])    
    
    P = sorted(list(permutations(setA,n)))
    
    for i in xrange(len(P)):
        print ''.join(P[i])