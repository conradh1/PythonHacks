#!/usr/bin/python
#This python program encrypts a string to rot13 encryption

#get string to encrypt from standard input
str= raw_input("enter a string to encrypt:")
place= 5
output= "Encrypted text: "
for i in range(len(str)):
	ascii_num = ord(str[i]) #get ASCII number of character
	if (ascii_num >= ord('A')) and (ascii_num <= ord('Z')):	
		#push the character 13 places and modulus 26 to keep in range
		ascii_num = ((ascii_num - ord('A') + place) % 26 + ord('A'))
	elif (ascii_num >= ord('a')) and (ascii_num <= ord('z')):
		ascii_num = ((ascii_num - ord('a') + place) % 26 + ord('a'))
	char= chr(ascii_num) #convert ASCII ascii_num to character
	output= output+char #add encrypted character
print output
