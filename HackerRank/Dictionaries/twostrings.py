#!/bin/python

import math
import os
import random
import re
import sys
import string
# Complete the twoStrings function below.
def twoStrings(s1, s2):
    found = False
    alphabet_string = string.ascii_lowercase
    alpha = list(alphabet_string)

    for i in range(0, len(alpha)):
        if (alpha[i] in s1 and alpha[i] in s2):
            found = True
            break

    if (found):
        return('Yes')
    else:
        return('No')

if __name__ == '__main__':
    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = twoStrings(s1, s2)

        print(result)
