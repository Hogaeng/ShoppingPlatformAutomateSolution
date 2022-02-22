#-*- coding:cp949 -*-
from lxml import html  
import csv,os,json
import requests
import json
import re
url="https://smartstore.naver.com/cottondeco/products/4510966433"
r=requests.get(url)
t=html.fromstring(r.content)
title=t.xpath('/html/head/title/text()')
speaker=t.xpath("/html/body/script[1]/text()")
print(title)
d=re.search(r'window\.__PRELOADED_STATE__=({.*})',r.text).group(0)
with open('raw2.json', 'w') as writer:
    writer.write(d)

j=json.loads(d)
print(j['product']['A']['channel']['naverPaySellerNo'])