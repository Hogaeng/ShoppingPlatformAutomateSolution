import hmac
import hashlib
import base64
import urllib.parse
vendorId="A00008673"
datetime="220221T040147Z"
method = "GET"
key = "adc4ccac20a3b688a7127b9439716afe0c8209c5"
path = "/v2/providers/seller_api/apis/api/v1/marketplace/seller-products"
query = urllib.parse.urlencode({"vendorId": vendorId, "maxPerPage": 100, "nextToken": 1, "status": "APPROVED"})
message = datetime+method+path+query
h = hmac.new(key.encode('utf-8'),message.encode('utf-8'),hashlib.sha256)
print(h.hexdigest())
if h.hexdigest()=="0839874d48d505938d8a94f9141def74d1efb4f51fe225321653628eb9556ae3":
    print("true")
else:
    print("False")