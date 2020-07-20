#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json

strAppToken = "" #Removed from public

objReq = urllib.request.Request("https://api.waqi.info/feed/beijing/?token="+strAppToken)

with urllib.request.urlopen(objReq) as objResponse:
   objPage = objResponse.read()

objData = json.loads(objPage)

intPM25Count = int(objData['data']['iaqi']['pm25']['v'])
strRecieveTime = objData['data']['time']['s']

print ("City: Beijing")
print ("PM2.5:", intPM25Count)
print ("Last Update:", strRecieveTime)
