#!/usr/bin/python

import urllib
try:
    import json
except ImportError:
    import simplejson as json

rawData = urllib.urlopen("http://google.ca")
print str(rawData)
