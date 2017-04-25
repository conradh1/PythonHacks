#!/usr/bin/python

#Basic operations
a = 7
b = 6

print "#### Basic Operations #####"
print a*b
print (a*b)/10.0
print a%2
#Bitwise operations
print "#### Bitwise Operations #####"
x = 3 #0011
y = 4 #0100
print x << 2 #shift left two bits: 1100
print x | y #bitwise OR: 0111
print x & y #bitwise AND: 0000

#Complex Numbers
print "#### Complex Operations #####"

import math
pi= math.pi
print "PI to two decimal places: %.2f" % (pi)
print "2 to the 4th power: %d" % pow(2,4)
print "Absolute value of -42: %d" % abs(-42)
