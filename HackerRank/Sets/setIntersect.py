#!/usr/bin/python

#Python use of set intersection example
#See: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
import sys
import string

if __name__ == '__main__':
    n = int(raw_input())
    setA = set(map(int, raw_input().split()))
    m = int(raw_input())
    setB = set(map(int, raw_input().split()))
    total = len(setA.intersection(setB))
    print total