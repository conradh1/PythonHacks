#!/bin/python
#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys


# simple array marching:
def march(arr):

    # simple 1...n
    print "March forward"
    for i in range(0,len(arr),1):
        print("%d " % arr[i]),

    print "\nMarch backward"
    # simple n.. 1
    for i in range(len(arr)-1, -1,-1):
        print("%d " % arr[i]),
    print "\n"
# simple quick sort in arrays. best case log(n) wost case n^2
def quicksort(arr, low, high):
    i = low
    j = high
    pivot = arr[random.randint(low, high)]

    while (i <= j):
        while (arr[i] < pivot):
            i += 1
        while (arr[j] > pivot):
            j -= 1
        if (i <= j):
            # swap
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j -= 1

    # call quickSort() method recursively
    if (low < j):
        quicksort(arr, low, j)
    if (i < high):
        quicksort(arr, i, high)
    return arr

# dictionaries

def capitals():
    # Create empty dict Capitals
    Capitals = dict()

    # Fill it with some values
    Capitals['Russia'] = 'Moscow'
    Capitals['Ukraine'] = 'Kiev'
    Capitals['USA'] = 'Washington'

    Countries = ['Russia', 'France', 'USA', 'Russia']

    for country in Countries:
      # For each country from the list check to see whether it is in the dictionary Capitals
        if country in Capitals:
            print('The capital of ' + country + ' is ' + Capitals[country])
        else:
            print('The capital of ' + country + ' is unknown')

    print Capitals.items()
    print Capitals.keys()
    Capitals.pop('USA')


def march2D():

    arr = [[1, 2, 3], [4, 5, 6]]
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            print (arr[i][j]),
        print "\n"


# Complete the minimumSwaps function below.
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #arr = map(int, raw_input().rstrip().split())


    #march(arr)
    #print(quicksort(arr, 0, len(arr)-1))
    #march2D()
    capitals()
