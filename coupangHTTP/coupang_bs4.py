from bs4 import BeautifulSoup
import requests
import re

url="https://www.coupang.com/vp/products/256736665/breadcrumb-gnbmenu"
header={'User-Agent' :"Python/3.9.7"}
r=requests.get(url,headers=header)
#t=html.fromstring(r.content)
soup = BeautifulSoup(r.text, 'html.parser')
li=soup.find_all("a",{'class':'breadcrumb-link'})
for i in range(0,len(li)):
    li[i]=re.sub("<(.*?)>","",str(li[i]))
    li[i]=re.sub("\n *","",str(li[i]))
print(li)