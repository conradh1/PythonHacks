#!/usr/bin/python

#Python Given a string mutable the string
#See: https://www.hackerrank.com/challenges/python-mutations/problem
import sys
import string


def mutate_string(string, position, character):
    mylist = list(string)
    mylist[position] = character
    return "".join(mylist)

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()  #Split two args, position and replace character.
    s_new = mutate_string(s, int(i), c)
    print s_new