
#-*- coding:cp949 -*-
from lxml import html  
import csv,os,json
import requests
import json
url="https://smartstore.naver.com/ckheavenly/products/4293845034"
#url="https://smartstore.naver.com/i/v1/reviews/paged-reviews?page=1&pageSize=20&merchantNo=510305944&originProductNo=4285803200&sortType=REVIEW_RANKING"
r=requests.get(url)
t=html.fromstring(r.content)

title=t.xpath('/html/head/title/text()')
#Create the list of speaker
speaker=t.xpath("/html/head/script[1]/text()")
#speaker=t.xpath("/html/body/script[1]/text()")
print(title)
#print(speaker)
#print(len(speaker))
j=json.loads(speaker[0])
print(j)
