#!/bin/python

import sys

#See: https://www.hackerrank.com/challenges/pairs/problem

def pairs(k, arr):
	return len(set(arr) & set(x + k for x in arr))

if __name__ == "__main__":
	n, k = raw_input().strip().split(' ')
	n, k = [int(n), int(k)]
	arr = map(int, raw_input().strip().split(' '))
	result = pairs(k, arr)
	print result
