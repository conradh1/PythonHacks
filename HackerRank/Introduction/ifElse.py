# See: https://www.hackerrank.com/challenges/py-if-else?h_r=next-challenge&h_v=zen

import sys

num = int(raw_input())

if ( num % 2 != 0 ):
	print("Weird")
elif ( (num >= 2 and num <= 5) and num % 2 == 0 ):
	print("Not Weird")
elif ( (num >= 6 and num <= 20) and num % 2 == 0 ):
	print("Weird")
elif ( num > 20 and num % 2 == 0 ):
	print("Not Weird") 


