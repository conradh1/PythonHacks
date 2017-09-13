#!/usr/bin/python

#Python measure difference in sets
#See: https://www.hackerrank.com/challenges/no-idea/problem
import sys
import string


def totalHappiness(a,b,h):    
    happy = sum([(i in a) - (i in b) for i in h])
              
    return happy

if __name__ == '__main__':
    n, m = raw_input().split()
    h = raw_input().split()

    a = set(raw_input().split())
    b = set(raw_input().split())
    print totalHappiness(a,b,h)