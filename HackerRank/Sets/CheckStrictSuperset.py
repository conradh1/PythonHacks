#!/usr/bin/python

#Python Returns true or false based on a superset
#See: https://www.hackerrank.com/challenges/py-check-strict-superset?h_r=next-challenge&h_v=zen
import sys
import string


superSet= [] #list of True/False for each subset.

def isSuperSet(A, B):
	#compare is A is a subset of B
	return A.issuperset(B)

if __name__ == '__main__':
	superSet = set(map(int,raw_input().split()))
	isSuper = True
	for i in range(int(raw_input())):
		S = set(map(int, raw_input().split()))
		isSuper = isSuperSet(superSet,S )
		if (isSuper == False):
			break

print isSuper
