#!/bin/python

#https://www.hackerrank.com/challenges/time-conversion/problem
import sys
import time

def timeConversion(s):
	pattern = '%I:%M:%S%p'
	#covert to epoch
	epoch = int(time.mktime(time.strptime(s, pattern)))
	# convert epoch to 24 example 07:05:45PM becomes 19:05:45
	time24 = time.strftime("%H:%M:%S", time.localtime(epoch))
	return time24
    

s = raw_input().strip()
result = timeConversion(s)
print(result)
