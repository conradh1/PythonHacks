#!/bin/python

import sys

# See HackerRank: https://www.hackerrank.com/challenges/sherlock-and-array/problem

def solve(arr):
	# Complete this function
	total_left = 0
	total_right = 0
	mid = len(arr)/2
    
	if ( len(arr) == 1):
		return "YES"
	answer = "NO"
	for i in range(0,len(arr)):
		if ( i < mid):
			total_left += arr[i]
		if ( i > mid):
			total_right += arr[i]
			
	#print "debug: left"+str(total_left)+" right"+str(total_right)+" mid"+str(mid)
    
	while (mid >= 0 and mid < len(arr)-1  ) :
		#print "debug"+str(mid)
		if ( total_left == arr[mid] and total_right == arr[mid] ):
			answer = "YES"
			break
		elif (total_left > total_right):
			total_right += arr[mid]
			mid -= 1
			total_left -= arr[mid]
		elif (total_left < total_right):
			total_left += arr[mid]
			mid += 1
			total_right -= arr[mid]
		else:
			break
	return answer

T = int(raw_input().strip())
for a0 in xrange(T):
	n = int(raw_input().strip())
	arr = map(int, raw_input().strip().split(' '))
	result = solve(arr)
	print(result)

