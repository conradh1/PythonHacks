#!/usr/bin/python

#Python Read four numbers a, b, c, and d, and print the result of a^b + c^d. 
#See: https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
import sys
import string
import math


def printFormula(a,b,c,d):    
    #x = int(math.pow(a,b)+math.pow(c,d))
    x = a**b+c**d
    print str(x)
    
    #4710194409608608369201743232

if __name__ == '__main__':    
    
    a = int(raw_input())
    b = int(raw_input())
    c = int(raw_input())
    d = int(raw_input())
    printFormula(a,b,c,d)
