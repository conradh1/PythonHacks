#!/usr/bin/python

for x in range(1, 33):
	if ( x < 10):
		i = '0'+str(x)
	else:
		i = str(x)
	print "select * from [lm"+i+"].[Cold_PS1_PV3_"+i+"].dbo.[Detection] "
	print "union all"
