# See: https://www.hackerrank.com/challenges/write-a-function?h_r=next-challenge&h_v=zen

import sys

n = int(raw_input())

def print_function(num):
	for i in range(1,num+1):
		sys.stdout.write(str(i))
	print
# end is_leap

print_function(n)
