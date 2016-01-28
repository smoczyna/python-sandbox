#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "58128"
__date__ = "$14-Dec-2015 09:21:37$"

#import requests
#response = requests.get("http://10.30.67.130:18004/esblogs1/PolarLake", stream=True)
#
#from java.util import TreeSet
#logs = TreeSet();
#logs.add(response.iter_content(512))
#print len(logs)

#print(logs)
#print(response.iter_content(512))

import urllib2  # the lib that handles the url stuff

targetURL = 'http://10.30.67.130:18004/esblogs1/PolarLake'

#data = urllib2.urlopen(targetURL) # it's a file like object and works just like a file
#for line in data: # files are iterable
#    print line

data = urllib2.urlopen(targetURL).read(20000) # read only 20 000 chars
data = data.split("\n") # then split it into lines

for line in data:
    print line    