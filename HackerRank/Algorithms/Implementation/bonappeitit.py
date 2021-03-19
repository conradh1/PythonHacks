#!/bin/python

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total = 0

    for i in range(0,len(bill)):
        if (i != k):
            total += bill[i]
    owe = (total)/2
    diff = b - owe
    if ( diff > 0 ):
        print(str(diff))
    else:
        print ('Bon Appetit')

if __name__ == '__main__':
    nk = raw_input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = map(int, raw_input().rstrip().split())

    b = int(raw_input().strip())

    bonAppetit(bill, k, b)
