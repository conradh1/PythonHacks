#!/usr/bin/python
#This python program sees many attempts to win the lottery/

#get string to encrypt from standard input

from random import sample
import time

def get_raffle( ticket ):
	raffle = sample(range(1,49), 6)
	raffle.sort()
	winner = False
	if (ticket == raffle):
		winner = True
	#else:
		#print "loser: "+result
	return winner


print "Let's play the lottery."
ticket_input= raw_input("Enter six digit between 1-49 sepearated by a space. Order is not important.\n")
ticket= []

# conver to integer list
for x in ticket_input.split(' '):
	ticket.append(int(x))

ticket.sort()
winner = False

attempts = 0

print "Playing Lottery.... Be patience"

while (winner == False):
	attempts += 1
	winner = get_raffle(ticket)

print "You won in "+str(attempts)+" attempts."
