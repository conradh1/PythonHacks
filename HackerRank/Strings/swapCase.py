#!/usr/bin/python

#Python Changes upper case letter to lower and vise-versa
#See: https://www.hackerrank.com/challenges/swap-case/problem
import sys
import string


def swap_case(s):
    wList = list(s)
    newWord = "";
    for i in range(len(wList)):
        letter = wList[i]
        if ( letter.isupper() ):
            newWord += letter.lower()
        elif ( letter.islower() ):
            newWord += letter.upper()
        else:
            newWord += letter
    return newWord

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result