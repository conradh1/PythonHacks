#!/bin/python3

import sys
import re

def super_reduced_string(s):
    p= re.compile(r'(\w)\1{1}',re.I)
    m = p.search(s)
    while(m):
        s = p.sub("", s,count=1)
	m= p.search(s)
	
    if ( s == ''):
        s = 'Empty String'
    return s

s = raw_input();
result = super_reduced_string(s)
print(result)