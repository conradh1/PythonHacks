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
