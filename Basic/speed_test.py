#!/usr/bin/python
#simple regular expression manipulation

import re #regular expression library
import time
import random #random number generator library

def strTest(limit):
#appends a long string
	tmp= "";
 	for i in range(limit):
    		tmp= tmp+"Appending a String %d \n" % i
#end strTest
def loopTest(limit):
#performs a loop test
	for i in range(limit):
    		pass
#end loopTest
def stdoutTest(limit):
#prints several message to stdout
	for i in range(limit):
		print "Printing to stdout."
#end stdoutTest
def mathTest(limit):
#appends several a set of random numbers (1-10)
	sum= 0;
	for i in range(limit):
		sum= sum+random.randrange(1,10)
#end mathTest

def objectTest(limit):
	class ObjTest: pass

	for i in range(limit):
		test=ObjTest()
		for j in range(10000):
			test.next=ObjTest()
			test=test.next
#end objectTest
######################### Main Program ################
print "Performing String Test...\n"
before= time.time()
strTest(1000)
after= time.time()
str_test= (after - before)*1000
#######################################################
print "Performing Loop Test...\n"
before= time.time()
loopTest(10000)
after= time.time()
loop_test= (after - before)*1000
#######################################################
print "Performing Standard Output Test...\n"
before= time.time()
stdoutTest(1000)
after= time.time()
stdout_test= (after - before)*1000
#######################################################
print "Performing Math Test...\n"
before= time.time()
stdoutTest(10000)
after= time.time()
math_test= (after - before)*1000
#######################################################
print "Performing Object Test...\n"
before= time.time()
objectTest(1000)
after= time.time()
obj_test= (after - before)*1000
#######################################################
print "##########################################################"
print "########### Time Results For Each Test in Python #########"
print "##########################################################"
print "String appending test= %.0f milliseconds." % str_test
print "Loop test= %.0f milliseconds." % loop_test
print "Standard Output test= %.0f milliseconds." % stdout_test
print "Math test= %.0f milliseconds." % math_test
print "Object generation test= %.0f milliseconds." % obj_test