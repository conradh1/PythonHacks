#!/usr/bin/python

#Python List manipulation example
#See: https://www.hackerrank.com/challenges/nested-list
import sys
import string

grades = {}

# print all second lowerest scores.
def secondLow():
	names = []	
	
	x = 0.0
	y = 0.0
	first = True

	for name, score in grades.items():
		if ( first ):
			x = score
			y = score
			first = False
		if (score < x):
			y = x
			x = score					
			# if (len(names) > 0):				
			# 	if (grades[names[0]] > score ):
			# 		names = []
			#names.append(name)

	#return names
	return y

if __name__ == '__main__':
	n = int(raw_input())

	for _ in range(0,n):
		name = raw_input()
		score = float(raw_input())
		grades[name]= score
	
	names = secondLow()
	print(""+str(names))
	# for name in names:
	#  	print name


