#!/usr/bin/python
from SOAPpy import SOAPProxy
from SOAPpy import WSDL

import sys

print "########## PSPS Query Client ############"
user = 'psps_tester'
password = '!psps!'
wsdlFile = 'http://svn.pan-starrs.ifa.hawaii.edu/repo/ipp/trunk/Nebulous/nebclient/nebulous.wsdl'
dynamicWsdlFile = 'http://ambon.ifa.hawaii.edu:8080/Mleadr/AuthService?wsdl'
namespace = 'urn:Nebulous/Server/SOAP'
queryFileName = sys.argv[1]
resultFileName = sys.argv[2]
print "Found query file: ", queryFileName
print "Found result file: ", resultFileName
#print 'Attempting to Authenticate' #comment here
query = open(queryFileName, 'r').read()

server = SOAPProxy(wsdlFile, namespace)
#server = WSDL.Proxy(wsdlFile) 
#sessionID = server.login(user, password)
server.methods.keys()
results = query
resultFile = open(resultFileName, "w")
resultFile.write(results)
resultFile.close

print "Done!"