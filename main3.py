import requests
# from urllib.parse import urlencode
import hashlib
import datetime


url = 'https://s3papidoc.smobilpay.maviance.info/v2'  
headers = {'Accept': 'application/json'}
api_key = '959F4A67-A093-1358-5FE1-D1C9AF3F026F'
api_secret = 'F6D427E3-C069-DE62-7E93-FB384DC18A30'

Authorization: s3pAuth,s3pAuth_nonce="634968823463411609",s3pAuth_signature="V5F+YLj2vQNTfZrmg3OYPFZJ4hw=",s3pAuth_signature_method="HMAC-SHA1",s3pAuth_timestamp="1361281946",s3pAuth_token="xvz1evFS4wEEPTGEFPHBog" 
timestamp = str(datetime.datetime.utcnow().isoformat())
signature = hashlib.sha256((timestamp + api_secret).encode()).hexdigest()


headers = {
    "X-API-KEY": api_key,
    "X-API-TIMESTAMP": timestamp,
    "X-API-SIGNATURE": signature,
    "Accept": 'application/json'
}

params = {
    'x-api-version': '3.0.0'
    }



response = requests.get(url, params=params,  headers=headers, verify=False)


if response.status_code == 200:
    data = response.json()
    # Traiter les données
else:
    print(f"Erreur : {response.status_code}")

