#!/usr/bin/python

#Python average of unique heights.
#See: https://www.hackerrank.com/challenges/symmetric-difference/problem
import sys
import string


def showDifference(a,b):    
    diff = list(sorted(a ^ b))
    
    for i in range(len(diff)):
        print diff[i]

if __name__ == '__main__':
    i = input()
    l1 = set(map(int, raw_input().split()))
    j = input()
    l2 = set(map(int, raw_input().split()))
    showDifference(l1,l2)