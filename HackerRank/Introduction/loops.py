# See: https://www.hackerrank.com/challenges/python-arithmetic-operators?h_r=next-challenge&h_v=zen

import sys

num = int(raw_input())

#f = str(float(a)/b)

if (num > 20):
	print "Error: Number "+str(num)+" too big."
	exit()

for i in range(0,num):
	print str(pow(i,2))
