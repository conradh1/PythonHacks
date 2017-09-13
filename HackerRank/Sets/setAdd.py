#!/usr/bin/python

#Python use of add Operation
#See: https://www.hackerrank.com/challenges/py-set-add/problem
import sys
import string


if __name__ == '__main__':
    setCountry = {}; # use as set
    setCountry = set()
    n = int(raw_input())
    total = 0
    for i in range(n):
        country = raw_input()
        if (country not in setCountry):
            setCountry.add(country)
            total += 1
    print total