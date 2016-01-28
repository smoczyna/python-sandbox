#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "58128"
__date__ = "$28-Jan-2016 12:25:35$"


#<?xml version="1.0" encoding="UTF-8"?>
#<Request>
#        <Log/>
#        <ID>
#                <AppID/>
#                <AppName/>
#                <UsrID/>
#                <UnqID/>
#        </ID>
#        <sourceNSC/>
#        <staffNumber>89876</staffNumber>
#        <AMessage>......</AMessage>
#</Request>

import urllib
import urllib2

#dslURL = "http://localhost:8080/dsl/service"
dslURL = "http://omgasnbpint:9085/dsl-inttest/service"

serviceName = "Signon"
strPayload = '<?xml version="1.0" encoding="UTF-8"?><Request><Log>P</Log><ID><version>1.0</version><AppID>NBP</AppID><AppName>null</AppName><UsrID>-7b1c799a:152697c5ac7:-7ffe</UsrID><UnqID>88036</UnqID></ID><regionCode>ROI</regionCode><sourceNSC>000000</sourceNSC><staffNumber>58128</staffNumber><deviceId>NP</deviceId><Transaction>SignonUser</Transaction><TransactionVersion>1</TransactionVersion><SignonUser><password>null</password><checkPassword>false</checkPassword></SignonUser></Request>'

httpParams = {'Content-Type' : 'application/x-www-form-urlencoded',
              'Content-Length' : len(strPayload),
              'Payload' : strPayload}

data = urllib.urlencode(httpParams)
req = urllib2.Request(dslURL, data)
response = urllib2.urlopen(req)
resp = response.read()
print resp