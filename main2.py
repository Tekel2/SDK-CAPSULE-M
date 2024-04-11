import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1Session

# url = 'https://s3papidoc.smobilpay.maviance.info/v2/service' 
# url = 'https://s3p.smobilpay.staging.maviance.info/v2' 
url = 'https://s3papidoc.smobilpay.maviance.info/v2/merchant'
headers = {'Accept': 'application/json'}
api_key = '959F4A67-A093-1358-5FE1-D1C9AF3F026F'
api_secret = 'F6D427E3-C069-DE62-7E93-FB384DC18A30'


oauth = OAuth1Session(api_key, api_secret)
response = oauth.get(url)


m_headers={
    'Authorization': 'key '+api_key,
    'Content-Type': 'application/json'
}

params = {
    'x-api-version': '3.0.0'
    }
auth = HTTPBasicAuth(api_key, api_secret)
# response = requests.get(url, headers=headers, auth=auth)
response = requests.get(url, params=params, headers=m_headers)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")