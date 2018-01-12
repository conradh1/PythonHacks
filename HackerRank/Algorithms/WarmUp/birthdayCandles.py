#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
	cmax = sys.maxint * -1
	total = 0;
    
	for i in range(len(ar)):
		if ( ar[i] > cmax):
			cmax = ar[i]
			total = 1
		elif ( ar[i] == cmax ):
			total += 1

	return total

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
