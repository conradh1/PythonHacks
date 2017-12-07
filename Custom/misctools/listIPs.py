#!/usr/bin/env python
#
# does a nslookup on a list of domains
#

import sys
import subprocess
import string
import re

prefix = "dx"
base_domain = "psps.ifa.hawaii.edu"
num = 16
p= re.compile("(\d{3}\.\d{3}\.\d{3}\.\d{3})",re.I | re.S)

for i in range(1,num+1):        
	full_domain = prefix+str(i).zfill(2)+'.'+base_domain
        result = subprocess.Popen(['nslookup', full_domain], stdout=subprocess.PIPE)
        ip = re.search('Address:[\s|\t]*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\n',result.stdout.read()).group(1)      
        print "Domain: "+full_domain+" Adress: "+ip
#endfor



