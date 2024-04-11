import requests


url = 'https://s3papidoc.smobilpay.maviance.info/v2'  
# headers = {'Accept': 'application/json'}
api_key = '959F4A67-A093-1358-5FE1-D1C9AF3F026F'
api_secret = 'F6D427E3-C069-DE62-7E93-FB384DC18A3'


url_enpoint = 'https://dev.smobilpay.com/s3p/v2/quotestd'
headers = {
    'Authorization': f'ApiKey {api_key}:{api_secret}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.text)
