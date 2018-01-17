#!/bin/python

# Hacker Rank Problem Missing Numbers
# See: https://www.hackerrank.com/challenges/missing-numbers/problem


import sys

def missingNumbers(arr, brr):
	# Complete this function
	result = []
	arr.sort()
	brr.sort()
	j = 0
    
	for i in range(len(brr)):
		if (j < len(arr) and arr[j] == brr[i]): 
			j += 1
		else:
			if (not result or brr[i] != result[len(result)-1]):
				result.append(brr[i])
			
	return result
    

if __name__ == "__main__":
	n = int(raw_input().strip())
	arr = map(int, raw_input().strip().split(' '))
	m = int(raw_input().strip())
	brr = map(int, raw_input().strip().split(' '))
	result = missingNumbers(arr, brr)
	print " ".join(map(str, result))


