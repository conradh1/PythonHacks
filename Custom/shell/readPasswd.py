#!/usr/bin/python
#readPasswd.py
#This reads the /etc/passwd file and prints out users that do not use bash shell.
import sys
import array
import string
import re



file_name= "/etc/passwd"
myfile= open(file_name, "r")


while 1:
	tmp= myfile.readline()[:-1] #read line subtract \n
	if not tmp: break
	line = tmp.split(":",6)  #split the variables based on semicolon
	uname = line[0]  #first argument username
	hdir = line[5] #home directory
	uid = line[2] #uid 
	shell = line[6]  #command/shell
	matchObj = re.search( r'bash', shell, re.I)  #finds batch keyword in the shell variable
	
	if not ( matchObj   ):
            #does not use bash
            print uname+","+uid+","+hdir