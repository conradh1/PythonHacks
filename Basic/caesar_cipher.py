#!/usr/bin/python
#This python program encrypts a string to Caesar Cipher encryption

#get string to encrypt from standard input
str= raw_input("enter a string to encrypt:")
key= int(raw_input("enter a key (1-26):"))
output= "Encrypted text: "
for i in range(len(str)):
	ascii_num = ord(str[i]) #get ASCII number of character
	if (ascii_num >= ord('A')) and (ascii_num <= ord('Z')):	
		#push the character key places and modulus 26 to keep in range
		ascii_num = ((ascii_num - ord('A') + 13) % 26 + ord('A'))
	elif (ascii_num >= ord('a')) and (ascii_num <= ord('z')):
		ascii_num = ((ascii_num - ord('a') + 13) % 26 + ord('a'))
	char= chr(ascii_num) #convert ASCII ascii_num to character
	output= output+char #add encrypted character
print output
