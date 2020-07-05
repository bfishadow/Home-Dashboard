#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json

strAppToken = "0528b84ab14a4c70ca646a160502c79f73345c6e"
objReq = urllib.request.Request("https://api.waqi.info/feed/beijing/?token="+strAppToken)

with urllib.request.urlopen(objReq) as objResponse:
   objPage = objResponse.read()

objData = json.loads(objPage)

intPM25Count = objData['data']['iaqi']['pm25']['v']

print(intPM25Count)
