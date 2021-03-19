#!/usr/bin/python

#Python use of set Operations
#See: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
import sys
import string

def doOps(setN, commands):
    
    # execute discard(), .remove() & .pop()
    for i in range(len(commands)):
        command = commands[i].split(' ') # split command
        if (command[0] == 'pop'):
            setN.pop()            
        elif (command[0] == 'remove'):
            n = int(command[1])
            setN.remove(n)                    
        elif (command[0] == 'discard'):
            n = int(command[1])
            setN.discard(n) 
                        
    total = 0
    for j in setN:
        total += j
    return total

if __name__ == '__main__':
    n = int(raw_input())
    commands = {};
    setN = set(map(int, raw_input().split()))
    N = int(raw_input())
    for i in range(N):
        commands[i] = raw_input()
    print doOps(setN, commands)