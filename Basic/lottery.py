#!/usr/bin/python
#This python program sees many attempts to win the lottery/

#get string to encrypt from standard input
from random import randint

def get_raffle( ticket, ticket_length ):
	raffle = []
	for x in range(0,ticket_length):
		# doing lottery 1 -49 numbers
		raffle.append(randint(1,49))
	raffle.sort()
	result = ' '.join(map(str, raffle))
	winner = False
	if (ticket == result):
		winner = True
	#else:
		#print "loser: "+result
	return winner


print "Let's play the lottery."
ticket= raw_input("Enter six digit between 1-49 sepearated by a space. Order is not important.\n")
ticket_numbers= []

# conver to integer list
for x in ticket.split(' '):
	ticket_numbers.append(int(x))

ticket_numbers.sort()
ticket = ' '.join(map(str, ticket_numbers))
winner = False

attempts = 0

print "Playing Lottery.... Be patience"
while (winner == False):
	attempts += 1
	winner = get_raffle(ticket,len(ticket_numbers))

print "You won in "+str(attempts)+" attempts."
