#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    allLetters = True;

    note.sort()
    magazine.sort()
    m = dict()
    n = dict()
    for word in magazine:
        m.setdefault(word, 1)
        m[word] += 1

    for word in note:
        n.setdefault(word, 1)
        n[word] += 1
        if ( word not in m.keys() ):
            allLetters = False
            break
        elif (n[word] > m[word]):
            allLetters = False
            break

    if (allLetters):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)
