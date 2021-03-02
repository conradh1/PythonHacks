#!/bin/python

import sys


def miniMaxSum(arr):
    # Complete this function
	low = sys.maxint
	high = -1
	total = 0;

	for i in range(0,len(arr)):
		total += arr[i];
		if (arr[i] > high):
			high = arr[i]
		if (arr[i] < low):
			low = arr[i]
	print str(total-high)+' '+str(total-low)

if __name__ == "__main__":
	arr = map(int, raw_input().strip().split(' '))
	miniMaxSum(arr)
