# -*- coding: utf-8 -*-
from SOAPpy import *

#url = 'http://web02.psps.ifa.hawaii.edu/DFetch/WSDL/AuthService.wsdl.php'

url = 'http://web01.psps.ifa.hawaii.edu/DFetch/AuthService.cgi'

# define the namespace
namespace = 'http://web01.psps.ifa.hawaii.edu/AuthService'

server = SOAPProxy(url)

# if you want to see the SOAP message exchanged
# uncomment the two following lines

#server.config.dumpSOAPOut = 1
#server.config.dumpSOAPIn = 1

# we see here how to specify the parameter name in the call
# (String_1)

print 'Light sensor simulation: ' + server._ns(namespace).login(String_1 =
"Your message or e-mail")