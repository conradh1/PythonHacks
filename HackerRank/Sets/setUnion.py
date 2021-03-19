#!/usr/bin/python

#Python use of set Union example
#See: https://www.hackerrank.com/challenges/py-set-union/problem
import sys
import string

if __name__ == '__main__':
    n = int(raw_input())
    setA = set(map(int, raw_input().split()))
    m = int(raw_input())
    setB = set(map(int, raw_input().split()))
    total = len(setA.union(setB))
    print total