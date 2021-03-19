#!/usr/bin/python

#Python Splits a string based on spaces and replaces with dashes
#See: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
import sys
import string


def split_and_join(s):
    l = s.split(" ")
    newWord = "";
    #for i in range(len(wList)):
    return "-".join(l)

if __name__ == '__main__':
    s = raw_input()
    result = split_and_join(s)
    print result