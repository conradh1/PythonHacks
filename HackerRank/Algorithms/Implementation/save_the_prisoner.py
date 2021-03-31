#!/bin/python
# https://www.hackerrank.com/challenges/save-the-prisoner/problem

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    # int n: the number of prisoners
    # int m: the number of sweets
    # int s: the chair number to begin passing out sweets from
    return (s + m -  2) % n) + 1)


if __name__ == '__main__':

    t = int(raw_input())

    for t_itr in xrange(t):
        nms = raw_input().split()
        
        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(str(result))    
