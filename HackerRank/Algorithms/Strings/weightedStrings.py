#!/bin/python

# Hacker rank problem see: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

import sys


#!/bin/python

import sys

def setSets(letters,sets):
		 
	i = 0
	while i < len(letters):
		c = letters[i]
		num = ord(c)
		num = (num-97)%26+1 #get sets character
		total = 1
		
		while ( i+1 != len(letters) and c == letters[i+1]):
			i += 1
			total += 1

		if ( sets.has_key(num) ):
			# don't add smaller sets
			if (total >= sets[num]):
				sets[num] = total
		else:
			sets[num] = total
		i += 1
#end setSets

def inSet(x):

	for num in sets:
		if ( x == num):
			return True
		if ( x % num == 0 and (x / num) <= sets[num]):
			return True
	
	return False


answers = []
sets = {}
s = raw_input().strip()
letters = list(s)

setSets(letters,sets)
n = int(raw_input().strip())


for a0 in xrange(n):
	x = int(raw_input().strip())
	if (inSet(x)):
		answers.append("Yes")
	else:
		answers.append("No")
		
#for num in sets:
	#print str(num)+ ' '+str(sets[num])
for i in range(len(answers)):
	print answers[i]