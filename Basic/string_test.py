#!/usr/bin/python
#String manipulation examples
#simple string manipulation

alpha = 'abc'
beta = 'def'
gamma= "This is a short sentence."

print alpha+beta #concatenation
print len(alpha+beta) #length in number if characters
for item in alpha: print item; #step through each character
if "c" in gamma: print "Found the letter c in string: "+gamma #returns 1 true, 0 false
print "Use of Python's \t \"escape\" characters. \n "

print gamma[:4], gamma[5:7], gamma[8], gamma[-15:-10], gamma[16:] #prints indexes of strings
#gamma[:4] returns the start of the string (index 0) to index 3 not including index 4.
#gamma[5:7] returns index 5 to 6 not including index 7.
#gamma[8] returns index 8 alone.
#gamma[-15:-10] Counts backward from the last index and returns indexes 10 to 14.
#gamma[16:] returns index 16 to the last index.

import string #standard string module

print string.upper(alpha) #converts to uppercase
print string.find(beta, "ef") #returns index of substring
print string.atoi("42")+1 #convert from string to integer
print string.join(string.split(beta, "def"), "ghi")
