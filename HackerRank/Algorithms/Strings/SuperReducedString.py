#!/bin/python3

import sys
import re

def super_reduced_string(s):
    r = re.sub(r'(\w)\1{2}', "", s)
    print r

s = input().strip()
result = super_reduced_string(s)
print(result)