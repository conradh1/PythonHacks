#!/usr/bin/python

#Python use of set intersection example
#See: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
import sys
import string
from itertools import product

if __name__ == '__main__':
    setA = map(int,raw_input().split())
    setB = map(int,raw_input().split())
    
    AB = list(product(setA,setB))
    
    for i in xrange(len(AB)):
        print AB[i],