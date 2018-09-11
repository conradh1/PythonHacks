#!/bin/python

import sys

def miniMaxSum(arr):
    # Complete this function
	miniMin = sys.maxint
	miniMax = sys.maxint * -1
	miniSum = 0;
	minSum = 0;
	maxSum = 0;
	for i in range(len(arr)):
		n = arr[i]
		miniSum += n
		
		if ( n < miniMin ): miniMin = n
		if ( n > miniMax ): miniMax = n
    
	minSum = miniSum - miniMax
	maxSum = miniSum - miniMin
	print str(minSum)+' '+str(maxSum)

if __name__ == "__main__":
	arr = map(int, raw_input().strip().split(' '))
	miniMaxSum(arr)
