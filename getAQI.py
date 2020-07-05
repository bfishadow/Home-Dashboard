#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json

strLaserEggId = "" # Removed from public
strAppToken = "" # Removed from public

objReq1 = urllib.request.Request("http://api-ios.origins-china.cn:8080/topdata/getTopDetail?id="+strLaserEggId)
objReq2 = urllib.request.Request("https://api.waqi.info/feed/beijing/?token="+strAppToken)

with urllib.request.urlopen(objReq1) as objResponse1:
   objPage1 = objResponse1.read()
with urllib.request.urlopen(objReq2) as objResponse2:
   objPage2 = objResponse2.read()

# Home AQI
objData1 = json.loads(objPage1)
intPM25Count1 = int(objData1['pm2_5'])
strRecieveTime1 = objData1['recieveTime']

# Public AQI
objData2 = json.loads(objPage2)
intPM25Count2 = objData2['data']['iaqi']['pm25']['v']
strRecieveTime2 = objData2['data']['time']['s']

## Print out
print ("Home AQI")
print ("ID:", strLaserEggId)
print ("PM2.5:", intPM25Count1)
print ("Last Update:", strRecieveTime1)

print ("---")
print ("Public AQI")
print ("PM2.5:", intPM25Count2)
print ("Last Update:", strRecieveTime2)