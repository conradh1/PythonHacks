#!/usr/bin/env python
#
# generates a password on 
#

import sys
import random

num = input("Enter number of characters for your passwords (8 - 25): ")

password = ""

if not ( num >= 8 and num <= 25):
	sys.exit("Error: Wrong number of arguments (8-25).")  

for i in range(1,num):
	r = random.randint(32,126)
        c = chr(r)
	#print "New character: %c" % (c)
	password += str(c) # switch int to char and append.
#endfor

print "New Password: %s\n" % (password)
