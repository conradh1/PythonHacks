#!/usr/bin/python

#Python List manipulation example
#See: https://www.hackerrank.com/challenges/python-lists
import sys
import string

n = int(raw_input())


def lists(n):
  lis = []
  for i in range(0,n):
    c = raw_input()
    line = c.split(' ')
    command = line[0]
    #print "command "+line
    if ( command == 'print' ):
      print lis
    elif ( command == 'append' ):
      lis.append(int(line[1]))
    elif ( command == 'remove'):
      lis.remove(int(line[1]))
    elif ( command == 'insert'):
      lis.insert(int(line[1]),int(line[2]))
    elif ( command == 'pop'):
      lis.pop()
    elif ( command == 'sort'):
      lis.sort()
    elif ( command == 'reverse'):
      lis.reverse()
    else:
      print "Error: unkown command. Must be insert, print, remove, append, sort, pop, or reverse."
  #for
#lists

lists(n)

#ListA= ['h','bcd','a','efg']

#ListA= ListA+["ij"]; #concatenation
#ListA.append('k') #appends a member
#print ListA.index('a') #searches the array and prints the index number when found
#print len(ListA) #returns the number of members in the list
#ListA.sort() #sort a list of strings
#print ListA
##the del and slice operations below eliminates the need for pop or dequeue because
##specific indexes can be removed
#del ListA[len(ListA)-1] #removes the last element from the list.
#ListA[:2]= ['abc','d'] #replaces first two indexes with given values
#for item in ListA: print item #lists each index member in the list

#ListB= [1,3,2,7,6,4,5]; #a list of integers
#ListB.sort() #sort a list of integers
#ListB.reverse() #reverse the integers
#print ListB
