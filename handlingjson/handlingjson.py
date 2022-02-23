import os
import time
import hmac, hashlib
import urllib.parse
import urllib.request
import ssl
import json

os.environ['TZ'] = 'GMT+0'


#replace with your own accesskey
accesskey = "b73396f8-be18-460d-aea3-4db8dfa129d5"
#replace with your own secretKey
secretkey = "adc4ccac20a3b688a7127b9439716afe0c8209c5"

method = "GET"
nextToken="1"
vendorId="A00008673"
path = "/v2/providers/seller_api/apis/api/v1/marketplace/seller-products"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
datalst=[]
while nextToken!="":
    try:
        querydic = {"vendorId": vendorId, "maxPerPage": 100, "nextToken": nextToken, "status": "APPROVED"}
        query = urllib.parse.urlencode(querydic)
        datetime=time.strftime('%y%m%d')+'T'+time.strftime('%H%M%S')+'Z'
        message = datetime+method+path+query
        #********************************************************#
        #authorize, demonstrate how to generate hmac signature here
        signature=hmac.new(secretkey.encode(),message.encode(),hashlib.sha256).hexdigest()
        authorization="CEA algorithm=HmacSHA256, access-key="+accesskey+", signed-date="+datetime+", signature="+signature
        #print out the hmac key
        #********************************************************#
        url = "https://api-gateway.coupang.com"+path+"?%s" % query
        req = urllib.request.Request(url)
        req.get_method = lambda: method
        req.add_header("Content-type","application/json;charset=UTF-8")
        req.add_header("Authorization",authorization)
        resp = urllib.request.urlopen(req,context=ctx)
    except urllib.request.HTTPError as e:
        print(e.code)
        print(e.reason)
        print(e.fp.read())
    except urllib.request.URLError as e:
        print(e.errno)
        print(e.reason)
        print(e.fp.read())
    else:
        print(200)
        body = resp.read().decode(resp.headers.get_content_charset())
        data=json.loads(body)
        nextToken=data['nextToken']
        datalst+=(data['data'])

'''
import pandas as pd
df=pd.DataFrame(datalst)
df.to_excel('datalst.xlsx')
'''

'''
data={}
datalst=[]
with open('product_forhandlingjson.json','r',encoding='utf8') as read_file:
    data=json.load(read_file)
nextToken=data['nextToken']
datalst+=(data['data'])
print(datalst[0])
'''