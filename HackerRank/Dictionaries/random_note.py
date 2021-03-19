#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    allLetters = True;

    m = Counter(magazine)
    n = Counter(note)

    for word in n:
        if n[word] > m[word]:
            allLetters = False
            break

    if (allLetters):
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)
