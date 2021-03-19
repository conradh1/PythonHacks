#!/usr/bin/python

#Python You are given a string S. Your task is to capitalize each word of S.
#See: https://www.hackerrank.com/challenges/the-minion-game/problem
import sys
import string


def minion_game(word):
    vowels  = 'aeiou';
    v = 0;  # variables for score
    c = 0;
    
    for i in range(len(word)):             
        if ( word[i].lower() in vowels ):
            v += (len(s)-i)
        else:
            c += (len(s)-i)
                    
    if v > c:
        print "Kevin", v
    elif v < c:
        print "Stuart", c
    else:
        print "Draw"

if __name__ == '__main__':
     s = raw_input()
     minion_game(s)