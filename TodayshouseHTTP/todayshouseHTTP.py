from lxml import html
import csv,os,json
import requests
import json
url="https://ohou.se/productions/feed?query=%ED%8C%A8%EB%B8%8C%EB%A6%AD%ED%8F%AC%EC%8A%A4%ED%84%B0&search_affect_type=Typing&input_source=productions"


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
print(title[0].encode('utf8'))
#Create the list of speaker
data=t.xpath('/html/body/div/ul/li[1]/a/text()')
print(data)
#speaker=t.xpath("/html/body/script[1]/text()")
#print(len(speaker))
#j=json.loads(speaker[0])
#print(j)