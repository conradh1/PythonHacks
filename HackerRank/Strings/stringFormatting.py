#!/usr/bin/python

#String formatting
#See: https://www.hackerrank.com/challenges/python-string-formatting/problem
#Given an integer, , print the following values for each integer  from  to :

#Decimal
#Octal
#Hexadecimal (capitalized)
#Binary

import sys
import string
import textwrap

def print_formatted(n):
    
    w = len(bin(n)[2:])
    for i in range(1,n+1):
        # Decimal Octal Hex Binary
        myhex = str(hex(i))[2:].upper().rjust(w,' ')  #change to upper and get rid of 0x        
        mybin = str(bin(i))[2:].rjust(w,' ') #get rid of 0B prefix
        myoct = str(oct(i))[1:].rjust(w,' ') # get rif of 0 prefix
        mydec = str(i).rjust(w,' ')
        print mydec, myoct, myhex, mybin
        


if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
    