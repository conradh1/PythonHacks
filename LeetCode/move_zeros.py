#!/bin/python
#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def move_zeros(nums):

    #[0, 1 ,3 0, 12]
    #[1, 3 ,12, 0, 0]
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        elif count > 0:
            nums[i-count] = nums[i]
    for j in range(len(nums)-1,count, -1):
        nums[j] = 0

    return nums







if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = map(int, raw_input().rstrip().split())

    res = move_zeros(arr)
    print (str(res))
    #fptr.write(str(res) + '\n')

    #fptr.close()
