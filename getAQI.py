#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json

# IDs:
# 18131	Living Room
# 18782	Master Bedroom
# 18777	Guest Bedroom
# 21460	Sesame Bedroom

strLaserEggId = "18131"

objReq = urllib.request.Request("http://api-ios.origins-china.cn:8080/topdata/getTopDetail?id="+strLaserEggId)

with urllib.request.urlopen(objReq) as objResponse:
   objPage = objResponse.read()

objData = json.loads(objPage)

intPM25Count = int(objData['pm2_5'])
strRecieveTime = objData['recieveTime']

print ("ID:", strLaserEggId)
print ("PM2.5:", intPM25Count)
print ("Last Update:", strRecieveTime)