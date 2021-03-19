#!/usr/bin/python

#Python List manipulation example
#See: https://www.hackerrank.com/challenges/nested-list
import sys
import string

grades = []

for _ in range(int(raw_input())):
	name = raw_input()
	score = float(raw_input())
	grades.append([name,score])

low1 = 101.0
low2 = 101.0
low1Name = ''
low2Name = ''
secondLow = []
secondLow.append([low2Name, low2])

for i in range(0,len(grades)):
	#print grades[i][0]+" "+str(grades[i][1])
	name = grades[i][0]
	score = grades[i][1]

	if ( score < low1 ):
		low2 = low1
		low2Name = low1Name
		low1 = score
		low1Name = name
	elif ( score <= low2 and score > low1 ):
		low2 = score
		low2Name = name

	if ( secondLow[0][1] > low2 ):
			secondLow = []
			secondLow.append([low2Name, low2])
	elif ( secondLow[0][1] == low2 and secondLow[0][0] != low2Name ):
			secondLow.append([low2Name, low2])

# for

for i in range(0, len(secondLow)):
	#print "Second lowest: "+secondLow[i][0]+": "+str(secondLow[i][1])
	print secondLow[i][0]