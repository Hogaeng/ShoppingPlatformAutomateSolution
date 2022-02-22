
#-*- coding:cp949 -*-
from lxml import html
import csv,os,json
import requests
import json
urlrocket="https://www.coupang.com/vp/products/5497638313"
url="https://www.coupang.com/vp/products/256736665"


header={'User-Agent' :"Python/3.9.7"}

r=requests.get(url,headers=header)
t=html.fromstring(r.content)
'''
with open('nonrocket.html','w',encoding='utf8') as f:
    f.write(r.text)


r=requests.get(urlrocket,headers=header)
t=html.fromstring(r.content)
with open('rocket.html','w',encoding='utf8') as f:
    f.write(r.text)
'''
title=t.xpath('/html/head/title/text()')
print(title)
#Create the list of speaker
data=t.xpath('/html/body/div/ul/li[1]/a/text()')
print(data)
#speaker=t.xpath("/html/body/script[1]/text()")
#print(len(speaker))
#j=json.loads(speaker[0])
#print(j)