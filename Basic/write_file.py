#!/usr/bin/python
#write_file.py
#This is a python program that writes to a file

import sys
import string

print "Enter the file of the name to write to."
file_name= sys.stdin.readline() #get the name of the file from user
file_name= file_name[:-1] #get rid of \n

myfile= open(file_name, 'w') #open for output (creates)
myfile.write("Printed to file with Python.\n")
myfile.close()
#end program
