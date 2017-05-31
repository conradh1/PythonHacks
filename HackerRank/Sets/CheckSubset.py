#!/usr/bin/python

#Python Compares two subsets
#See: https://www.hackerrank.com/challenges/py-check-subset?h_r=next-challenge&h_v=zen
import sys
import string


subList= [] #list of True/False for each subset.

def checkSubset(A, B):
	#compare is A is a subset of B
	return (set(sorted(A)) < set(sorted(B)))

if __name__ == '__main__':
	for i in range(int(raw_input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.
		a = int(raw_input()); A = set(raw_input().split())
		b = int(raw_input()); B = set(raw_input().split())
		subList.append(checkSubset(A,B))

for i in range(len(subList)):
	print subList[i]
