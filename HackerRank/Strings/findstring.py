#!/usr/bin/python

#Python gives the number of substrings in a string
#See: https://www.hackerrank.com/challenges/find-a-string/problem
import sys
import string


def count_substring(string, sub_string):
    mylist = list(string)
    count = 0
    
    for i in range(0, len(string)):
        if ( string.find(sub_string, i) == i ):
            count += 1
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print count