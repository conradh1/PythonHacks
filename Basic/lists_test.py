#!/usr/bin/python

#Python List manipulation examples

ListA= ['h','bcd','a','efg']

ListA= ListA+["ij"]; #concatenation
ListA.append('k') #appends a member
print ListA.index('a') #searches the array and prints the index number when found
print len(ListA) #returns the number of members in the list
ListA.sort() #sort a list of strings
print ListA
#the del and slice operations below eliminates the need for pop or dequeue because
#specific indexes can be removed
del ListA[len(ListA)-1] #removes the last element from the list.
ListA[:2]= ['abc','d'] #replaces first two indexes with given values
for item in ListA: print item #lists each index member in the list

ListB= [1,3,2,7,6,4,5]; #a list of integers
ListB.sort() #sort a list of integers
ListB.reverse() #reverse the integers
print ListB
