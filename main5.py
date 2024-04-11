import hmac
import hashlib
import base64
from  urllib import parse
import secrets
import random
url = "https://www.exemple.com/ ceci est un test/"



def generate_hmac_sha1_signature(method, content_md5, content_type, date, resource):
    request_string = method + "&" + content_md5 + "&" + content_type + "&" + date + "&" + resource
    secret_key = "F6D427E3-C069-DE62-7E93-FB384DC18A3"
    signature = hmac.new(secret_key.encode(), request_string.encode(), hashlib.sha1).hexdigest()
    encoded_signature = base64.b64encode(signature.encode()).decode()
    return encoded_signature

# Exemple d'utilisation
method = "GET"
content_md5 = ""
content_type = "application/octet-stream"
date = "2023-03-08T12:00:00Z"
resource = "https://s3papidoc.smobilpay.maviance.info/v2"
encoded_url = parse.quote_plus(resource)
print("URL encodée:", encoded_url)

signature = generate_hmac_sha1_signature(method, content_md5, content_type, date, encoded_url)


print("Signature:", signature)

code = secrets.token_hex(11).upper()

authTitleKey = "s3pAuth"
authTokenKey = "s3pAuth_token"
authNonceKey = "s3pAuth_nonce"
authSignatureKey = "s3pAuth_signature"
authSignatureMethodKey = "s3pAuth_signature_method"
authTimeStampKey = "s3pAuth_timestamp"
separator = ", "
signatureMethod = "HMAC-SHA1"
HMAC_SHA1_ALGORITHM = "HmacSHA1"
nonce = secrets.token_hex(11).upper()
# timeStamp = String.valueOf(Instant.now().getEpochSecond());



print("valeur: ", code)
# authTitleKey + " " + authNonceKey + "=\"" + nonce + "\"" + separator + authSignatureKey + "=\""
#                 + signature + "\"" + separator + authSignatureMethodKey + "=\"" + signatureMethod + "\"" + separator
#                 + authTimeStampKey + "=\"" + timeStamp + "\"" + separator + authTokenKey + "=\"" + accessToken + "\"";
