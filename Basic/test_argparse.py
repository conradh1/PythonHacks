#!/bin/env python
import os
import sys
import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,help="display a square of a given number")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    parser.add_argument("-m", "--mood", help="increase output verbosity <mood_name>=<mood_value>'")

    args = parser.parse_args()
    answer = args.square**2
    if args.verbose:
        print "the square of {} equals {}".format(args.square, answer)
    if args.mood:
        #(setting, value) = args.mood.split('=', 1)
        #print "debug"+setting+ " debug 2"+value
        print "Your mood is "+args.mood
    else:
        print answer
