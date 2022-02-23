import os
import time
import hmac, hashlib
import urllib.parse
import urllib.request
import ssl
import json

'''
import pandas as pd
df=pd.read_excel("datalst.xlsx")
df=df['sellerProductId']
print(df)
'''
os.environ['TZ'] = 'GMT+0'
method = "GET"
#replace with your own accesskey
accesskey = "b73396f8-be18-460d-aea3-4db8dfa129d5"
#replace with your own secretKey
secretkey = "adc4ccac20a3b688a7127b9439716afe0c8209c5"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
datalst=[]
try:
    datetime=time.strftime('%y%m%d')+'T'+time.strftime('%H%M%S')+'Z'
    #replace with your own vendorId
    path = "/v2/providers/seller_api/apis/api/v1/marketplace/seller-products/457504890"
    message = datetime+method+path

    signature=hmac.new(secretkey.encode(),message.encode(),hashlib.sha256).hexdigest()
    authorization="CEA algorithm=HmacSHA256, access-key="+accesskey+", signed-date="+datetime+", signature="+signature

    url = "https://api-gateway.coupang.com"+path
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
    # 200
    print(200)
    body = resp.read().decode(resp.headers.get_content_charset())
    data=json.loads(body)
    with open('pp.json','w',encoding='utf8') as write_file:
        json.dump(data, write_file, ensure_ascii=False)
    
    '''
    data=data["data"]
    #옵션이름 추가
    #메인이미지 추가(이미지 호스팅 필요)
    #상세HTML 추가(이미지 호스팅 필요)
    for dic in data["items"]:
        print(dic[''])
    '''