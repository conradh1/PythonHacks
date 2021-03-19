#!/bin/python

import sys

def caesarCipher(s, k):
    wordList = list(s)
    encrypt = ""
    
    for i in range(len(wordList)):
        c = wordList[i]
        num = ord(c)
        if 97 <= num <= 122:
            encrypt = encrypt+chr(((num-97+k)%26)+97)
        elif 65 <= num <= 90:
            encrypt = encrypt+chr(((num-65+k)%26)+65)
        else: encrypt = encrypt+c
        
    return encrypt


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
result = caesarCipher(s, k)
print result