#!/usr/bin/python

#Python Given a string mutable the string
#See: https://www.hackerrank.com/challenges/string-validators/problem

#In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
#In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
#In the third line, print True if  has any digits. Otherwise, print False. 
#In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
#In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

import sys
import string


def validate_string(str):
    print any(c.isalnum()  for c in str)
    print any(c.isalpha() for c in str)
    print any(c.isdigit() for c in str)
    print any(c.islower() for c in str)
    print any(c.isupper() for c in str)
    #print str.isspace()
    #print str.istitle()
    

if __name__ == '__main__':
    s = raw_input()
    validate_string(s)
    