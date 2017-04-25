# test with typles
# See: https://www.hackerrank.com/challenges/python-tuples?h_r=next-challenge&h_v=zen

#!/usr/bin/python
n = int(raw_input())

integer_list = map(int, raw_input().split())

tup1 = tuple(integer_list)

print hash(tup1)

