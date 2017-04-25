#!/usr/bin/python

#Python List manipulation example
#See: https://www.hackerrank.com/challenges/python-lists
import sys
import string

n = int(raw_input())
arr = map(int, raw_input().split())

def secondLargestNumber(n,arr):
  high = arr[0]
  second = -sys.maxint-1
  for i in range(0,n):
    num = arr[i]
    if ( num > high ):
	second = high
	high = num
    elif ( num > second and num < high ):
	second = num
  #for
  return second
#lists

print secondLargestNumber(n,arr)
