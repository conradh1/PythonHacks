#!/usr/bin/python

#Python word wrap
#See: https://www.hackerrank.com/challenges/text-wrap/problem
import sys
import string
import textwrap

def wrap(string, max_width):
    wrapper =textwrap.fill(string,max_width)
    return wrapper


if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result