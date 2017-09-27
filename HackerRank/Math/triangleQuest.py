#!/usr/bin/python

#Python You are given a string S. Your task is to capitalize each word of S.
#See: https://www.hackerrank.com/challenges/python-quest-1/problem
import sys
import string


def printTriangle(n):    
    for i in range(1,n):        
        print str(i)*i;

if __name__ == '__main__':
    n = int(raw_input())
    printTriangle(n)
