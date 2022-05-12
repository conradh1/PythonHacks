#!/bin/python
"""
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information.
"""

import math
from collections import OrderedDict
import os
import random
import re
import sys


#open a file and determine the greatest stride.
def dino_csv(dino_file_1, dino_file_2):

    dinos = dict()
    speeds = OrderedDict()
    file_handle = open(dino_file_1, 'r+')
    lines = [line.strip() for line in file_handle.readlines()]
    file_handle.close()

    for i in range(1,len(lines)):        
        info = lines[i].split(',',3)               
        dinos[info[0]] = float(info[1]) #leg length
    
    file_handle = open(dino_file_2, 'r+')
    lines = [line.strip() for line in file_handle.readlines()]
    file_handle.close()

    for i in range(1,len(lines)):        
        info = lines[i].split(',',3)
        dino_name = info[0]
        stride_length = float(info[1])
        stance = info[2]
        
        if (stance == 'bipedal'):
            leg_length = dinos[dino_name]            
            
            speed = ((stride_length / leg_length) - 1) * math.sqrt(leg_length * 9.8)                         
            speeds[str(speed)] = dino_name

    
    speeds = OrderedDict(reversed(sorted(speeds.items())))
    for speed in speeds:
        print (speeds[speed]+" speed "+speed)
    

# Complete the minimumSwaps function below.
if __name__ == '__main__':
    dino_csv('dino_1.csv','dino_2.csv')
