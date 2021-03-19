#! /usr/local/bin/python
#

import Cookie

import os
import ughtml

# Create a cookie dictionary object
c1 = Cookie.Cookie()

# Create a cookie in c1
# This will be temporary and will disappear when the session is closed
c1["cracker"] = "hello"
# The RFC says you should always set this but it seems to work ok without it
c1["cracker"]["version"] = 1

# Create another one
# Make the browser store it for one hour
c1["bisquit"] = "whatever"
c1["bisquit"]["max-age"] = 3600 # Time to keep, in seconds
c1["bisquit"]["expires"] = 3600 # Obsolete, but Netscape still seems to require it
c1["bisquit"]["version"] = 1

# Print the headers that sets the cookies
print c1

# Print an ordinary html page
ughtml.printContentType()
ughtml.printHeaders("ug's Python cookie test")

# Print the cookie headers, as they were returned
print "<h3>Cookies set by this script</h3>"
print "<pre>"
print c1
print "</pre>"

# Load and print any cookies that were received
print "<h3>Received cookies</h3>"
try:
    cookie = os.environ["HTTP_COOKIE"]
except KeyError:
    print "No cookies were received"
else:
    print "HTTP_COOKIE="+cookie
    print "<p>"
    c2 = Cookie.Cookie()
    c2.load(os.environ["HTTP_COOKIE"])
    print "<pre>"
    print c2
    print "</pre>"

    print "If you run it more than once within"
    print "a session, the cookies set by this script"
    print "will also be received from the browser."

# Finish the page
ughtml.printFooter()