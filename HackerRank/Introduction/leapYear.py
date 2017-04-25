# See: https://www.hackerrank.com/challenges/write-a-function?h_r=next-challenge&h_v=zen

import sys

year = int(raw_input())

def is_leap(year):
	leap = False # assume not leap year.
    
    	if ( year < 1900):
		return leap
	if ( year % 4 == 0 ):
		leap = True
		if  (year % 100 == 0 and year % 400 != 0):
			leap = False
		
	return leap
# end is_leap

print is_leap(year)
