#!/usr/bin/python

#Python use of set combinations example
#See: https://www.hackerrank.com/challenges/itertools-combinations/problem
import sys
import string
from itertools import combinations

if __name__ == '__main__':
    myInput = raw_input().split() #input for string and number of combinations.
    setA = list(myInput[0]) 
    n = len(myInput[0]) #case no second argument
        
    if (len(myInput) == 2): 
        n = int(myInput[1])    
    
    
    for i in range(1,n+1):
        P = list(combinations(sorted(setA),i))
        for j in xrange(len(P)):
            print ''.join(P[j])