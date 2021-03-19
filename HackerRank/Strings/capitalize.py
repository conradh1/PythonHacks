#!/usr/bin/python

#Python You are given a string S. Your task is to capitalize each word of S.
#See: https://www.hackerrank.com/challenges/capitalize
import sys
import string


def capitalize(string):
    mylist = string.split(" ")
    capitalized_string = ""
    for i in range(len(mylist)):
        #ignore extra spaces
        if ( mylist[i] != ""):
            cap = mylist[i][0] #get first charater
            # if a-z uppercase
            if (cap.isalpha()): 
                capitalized_string += cap.upper()+mylist[i][1:]+" "
            else:
                capitalized_string += mylist[i]+" "
        else: 
            capitalized_string += " " #add extra space
        
    return capitalized_string

if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string