#!/usr/bin/python
##################################
# Python Version 1.5.2
# Module Name: cgi_funcs.py
# Author: Conrad Holmberg
# Created: May9/02
# This program is for testing client/server functions
##################################
import cgi, sys, pwd, socket, os #import cgi and systems python modules
############################################################################
def html_header():
	print "Content-type: text/html\n"
	print "<html><head><title>CGI Environment in Python</title></head>"
	print "<h3>CGI Environment in Python</h3><hr>"
	print "<BODY BGCOLOR='#DDDDDD' TEXT='000000'>"
############################################################################
def html_footer():
#print the html footer
	print "</body></html>"
############################################################################
def show_environment():
	#Copy the environment array pointer
	env = os.environ
	form = cgi.FieldStorage()
	print "<dl>"
	print "<h3>Form Information</h3>"
	for name in form.keys():
        	print "name: " + name + " value: " + form[name].value + "<BR>"
        print "<hr></dl>"
	print "<dl>"
	print "<h3>Environment Information</h3>"
	env_keys = env.keys()
	env_keys.sort()
	for e in env_keys:
		print "<dt>"+cgi.escape(e+'='+'"'+env[e]+'"')
		print"</dl>"
###################Start Program############################################
html_header()
show_environment()
html_footer()
###################End Program##############################################
