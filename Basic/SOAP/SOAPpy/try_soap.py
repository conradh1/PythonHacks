#!/usr/bin/python
# -*- coding: utf-8 -*-

import SOAPpy

url = 'http://web01.psps.ifa.hawaii.edu/DFetch/WSDL/AuthService.php.wsdl'
proxy = SOAPpy.WSDL.Proxy(url)

# show methods retrieved from WSDL
print '%d methods in WSDL:' % len(proxy.methods) + '\n'
for key in proxy.methods.keys():
    print key
print

#request = { 'userid':  'psps_tester',
#            'password':'!psps!' }

#sessionID = proxy.login( request )

#print sessionID