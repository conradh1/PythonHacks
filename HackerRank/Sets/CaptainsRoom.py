#!/usr/bin/python

#Python List programming problem
#See: https://www.hackerrank.com/challenges/py-the-captains-room?h_r=next-challenge&h_v=zen
import sys
import string

def findCaptain(k,roomList):
	for room in roomList:
		# if the guest room is not the expect number return the captain's room
		guests = roomList[room]
		if ( guests == 1):
			print(room)
			break

if __name__ == '__main__':
    k = int(raw_input())  # number of people in a group
    rooms =  raw_input().split() # split each number
    roomList = dict()
    for i in range(len(rooms)):
		room = rooms[i]
		if room in roomList:
			roomList[room] += 1
		else:
			roomList[room] = 1

findCaptain(k,roomList)




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
