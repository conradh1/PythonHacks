#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
# https://www.hackerrank.com/challenges/grading/problem
def gradingStudents(grades):
    # Write your code here
    for i in range(0, len(grades)):        
        diff = 0
        # check for fail
        while ( (grades[i]+diff) % 5 != 0):
            diff += 1
        if (diff < 3 and (grades[i]+diff) >= 40):
            grades[i]= grades[i]+diff
    return grades

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(raw_input().strip())

    grades = []

    for _ in xrange(grades_count):
        grades_item = int(raw_input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
