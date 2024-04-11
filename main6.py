import hmac
import hashlib
import base64
from  urllib import parse
import secrets
import time
import requests



url = 'https://s3papidoc.smobilpay.maviance.info/v2/merchant'
api_key = '959F4A67-A093-1358-5FE1-D1C9AF3F026F'
api_secret = 'F6D427E3-C069-DE62-7E93-FB384DC18A30'

# authTitleKey = "s3pAuth"
s3pAuth_nonce = secrets.token_hex(5).upper()
method = "GET"
s3pAuth_timestamp = str(int(time.time()))
s3pAuth_signature_method = 'HMAC-SHA1'
signatureMethod = 'HMAC-SHA1'

def getParameterString():
    glue = '&'
    dataStr = ''
    dataStr += 's3pAuth_nonce' + '=' +str(s3pAuth_nonce.strip())
    dataStr += glue
    dataStr += 's3pAuth_signature_method' + '=' +str(s3pAuth_signature_method).strip()
    dataStr += glue
    dataStr += 's3pAuth_timestamp' + '=' +str(s3pAuth_timestamp).strip()
    dataStr += glue
    dataStr += 's3pAuth_token' + '=' +api_key
    
    return  dataStr

print("getParameterString: ",getParameterString())


def requetString():
    glue = '&'
    dataStr = method.upper() + glue
    dataStr += parse.quote_plus(url.strip()) + glue
    dataStr += getParameterString()

    return dataStr

def HMACSignature():
    signature = hmac.new(api_secret.encode(), requetString().encode(), hashlib.sha1).hexdigest()
    return base64.b64encode(signature.encode()).decode()

print("signature: ", HMACSignature())




def headerAuthorization():
    dataStr = 's3pAuth'
    dataStr += ','
    dataStr += 's3pAuth_nonce=\"' + s3pAuth_nonce + '\", '
    dataStr += 's3pAuth_signature=\"' + HMACSignature() + '\", '
    dataStr += 's3pAuth_signature_method=\"' + signatureMethod + '\", '
    dataStr += 's3pAuth_timestamp=\"' + s3pAuth_timestamp + '\", '
    dataStr += 's3pAuth_token=\"' + api_key + '\"'
    return dataStr

print("headerAuthorization:", headerAuthorization())




headers = {
    "X-API-KEY": api_key,
    'Authorization': headerAuthorization(),
    # 'Content-Type': 'application/json'
}


response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    # Traiter les données
else:
    print(f"Erreur : {response.status_code}")