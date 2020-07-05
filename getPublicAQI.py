#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json

objReq = urllib.request.Request("https://api.waqi.info/feed/beijing/?token=0528b84ab14a4c70ca646a160502c79f73345c6e")

with urllib.request.urlopen(objReq) as objResponse:
   objPage = objResponse.read()

#print (objPage)
# JSON Sample:
# b'{"status":"ok","data":{"aqi":132,"idx":1451,"attributions":[{"url":"http://www.bjmemc.com.cn/","name":"Beijing Environmental Protection Monitoring Center (\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82\xe7\x8e\xaf\xe5\xa2\x83\xe4\xbf\x9d\xe6\x8a\xa4\xe7\x9b\x91\xe6\xb5\x8b\xe4\xb8\xad\xe5\xbf\x83)"},{"url":"https://waqi.info/","name":"World Air Quality Index Project"}],"city":{"geo":[39.954592,116.468117],"name":"Beijing (\xe5\x8c\x97\xe4\xba\xac)","url":"https://aqicn.org/city/beijing"},"dominentpol":"pm25","iaqi":{"co":{"v":5.5},"h":{"v":38},"no2":{"v":6},"o3":{"v":85.8},"p":{"v":997},"pm10":{"v":39},"pm25":{"v":132},"so2":{"v":0.6},"t":{"v":33},"w":{"v":3.6}},"time":{"s":"2020-07-05 13:00:00","tz":"+08:00","v":1593954000},"forecast":{"daily":{"o3":[{"avg":17,"day":"2020-07-03","max":40,"min":1},{"avg":7,"day":"2020-07-04","max":16,"min":1},{"avg":5,"day":"2020-07-05","max":14,"min":1},{"avg":7,"day":"2020-07-06","max":17,"min":1},{"avg":12,"day":"2020-07-07","max":31,"min":1},{"avg":26,"day":"2020-07-08","max":59,"min":1},{"avg":19,"day":"2020-07-09","max":31,"min":15}],"pm10":[{"avg":96,"day":"2020-07-03","max":122,"min":70},{"avg":77,"day":"2020-07-04","max":114,"min":56},{"avg":79,"day":"2020-07-05","max":119,"min":42},{"avg":55,"day":"2020-07-06","max":72,"min":30},{"avg":82,"day":"2020-07-07","max":119,"min":45},{"avg":69,"day":"2020-07-08","max":111,"min":47},{"avg":68,"day":"2020-07-09","max":116,"min":57},{"avg":85,"day":"2020-07-10","max":116,"min":58},{"avg":71,"day":"2020-07-11","max":86,"min":58}],"pm25":[{"avg":182,"day":"2020-07-03","max":232,"min":161},{"avg":172,"day":"2020-07-04","max":173,"min":155},{"avg":173,"day":"2020-07-05","max":214,"min":121},{"avg":142,"day":"2020-07-06","max":173,"min":90},{"avg":162,"day":"2020-07-07","max":172,"min":137},{"avg":150,"day":"2020-07-08","max":158,"min":137},{"avg":161,"day":"2020-07-09","max":173,"min":139},{"avg":188,"day":"2020-07-10","max":237,"min":158},{"avg":166,"day":"2020-07-11","max":188,"min":152}],"uvi":[{"avg":0,"day":"2020-07-03","max":4,"min":0},{"avg":1,"day":"2020-07-04","max":3,"min":0},{"avg":1,"day":"2020-07-05","max":5,"min":0},{"avg":1,"day":"2020-07-06","max":8,"min":0},{"avg":1,"day":"2020-07-07","max":6,"min":0},{"avg":1,"day":"2020-07-08","max":6,"min":0},{"avg":1,"day":"2020-07-09","max":2,"min":0}]}},"debug":{"sync":"2020-07-05T14:51:12+09:00"}}}'


objData = json.loads(objPage)

intPM25Count = objData['data']['iaqi']['pm25']['v']

print(intPM25Count)
