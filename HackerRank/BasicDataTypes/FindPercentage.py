#!/usr/bin/python

#Python List programming problem
#See: https://www.hackerrank.com/challenges/finding-the-percentage
import sys
import string

def findPercentage(name,marks):
	avg = 0.0
	total = 0.0
	n = len(marks)
	for i in range(n):
		total += marks[i]
	avg = total/n
	#print "name is "+name
	print('%.2f' % avg)

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
findPercentage(query_name, student_marks[query_name])




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
