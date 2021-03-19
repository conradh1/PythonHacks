#!/usr/bin/python
#read_file.py
#This is a python program that read a file
import sys

print "Enter name of file for reading."
file_name= sys.stdin.readline() #get the name of the file from user
file_name= file_name[:-1] #get rid of \n

myfile= open(file_name, "r")

while 1:
	line= myfile.readline()
	print line[:-1]
	if not line: break

#for line in file.readlines() #can be used to place all file lines into an array
#end program
