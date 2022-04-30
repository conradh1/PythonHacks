#!/usr/bin/python

#Python You are given a string S. Your task is to capitalize each word of S.
#See: https://www.hackerrank.com/challenges/capitalize
import sys
import string


def draw_mat(n,m):
    side = (m-3)/2
    center_str = '.|.'
    center_total = 1
    mid = n//2 + 1
    messg = 'WELCOME'    
    
    for i in range(1,n+1):
        if ( i == mid):
            center_size = (m-len(messg))//2            
            print('-'*(center_size)+messg+'-'*(center_size))
            center_total -= 2
            side += 3        
        elif ( i < mid):
            print('-'*side+(center_str*center_total)+('-'*side))
            center_total += 2
            side -= 3
        else:                    
            print('-'*side+(center_str*center_total)+('-'*side))
            center_total -= 2
            side += 3


        
        

if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    draw_mat(n,m)    