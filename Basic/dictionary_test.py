#!/usr/bin/python
#Python Dictionaries examples

myweek= ['days of the week','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
#example of a seven item dictionary
days_of_the_week = {
	    'Monday': 1,
	    'Tuesday': 2,
	    'Wednesday': 3,
	    'Thursday': 4,
	    'Friday': 5,
	    'Saturday': 6,
	    'Sunday': 7
}

dictionary_week= {}; #empty dictionary

for i in range(7,0,-1):
	print myweek[i], '\t', days_of_the_week[myweek[i]]
	dictionary_week[myweek[i]] = i #snytax is dictionary[key]= value

print "########################\n"
for key in dictionary_week.keys(): print key, '\t', dictionary_week[key]

print "########################\n", dictionary_week['Friday'] #prints 5
print "########################\n", dictionary_week.keys() #prints all keys
print "########################\n", dictionary_week.values() #prints all values

if dictionary_week.has_key('Saturday'):
	print "########################\nSaturday is a valid key!\n"
