#!/usr/bin/python

#Python average of unique heights.
#See: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
import sys
import string


def average(arr):
    items = set(arr) #gets rid of duplicates
    total = sum(items)
    return total/(len(items)*1.0)

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result