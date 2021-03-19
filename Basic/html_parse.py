#!/usr/bin/python
#simple regular expression manipulation

import re #regular expression library

def html_parse(str):
#gets rid of html tags
	p= re.compile(r"<[^>]+>",re.I | re.S)
	str = p.sub("", str)
    	return str
#end html_parse
def get_html_tags(str):
#get the html tags in a string
	tags= "";
	
	p= re.compile("<[^>]+>", re.I | re.S)
	m = p.search(str)
	i=0;
	while(m):
		i= i+1
		tags= tags+m.group()
		str = p.sub("", str,count=1)
		m= p.search(str)
	return(tags)
#get_html_tags
######################### Main Program ################
html_str= "<html><head><body>This is some text.</body></head></body>"
print "The string before html parsing: ", html_str
print "The string after html parsing: ", html_parse(html_str)
print "The html tags that were parsed: ", get_html_tags(html_str)



