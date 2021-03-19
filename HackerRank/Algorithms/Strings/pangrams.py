#!/usr/bin/python

# HackerRank problem: https://www.hackerrank.com/challenges/pangrams/problem

import sys

def pangram(sentence):
    alpha = {}
    letters = list(sentence.lower())
        
    for i in range(len(letters)):
        c = letters[i]
        
        if ( c != ' '):
            if ( alpha.has_key(c) ):
                alpha[c] = alpha[c]+1
            else:
                alpha[c] = 1
                
    if ( len(alpha) == 26 ):
        print "pangram"
    else:
        print "not pangram"
    



s = raw_input().strip()
pangram(s)
