import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certification errors
cxt = ssl.create_default_context()
cxt.check_hostname = False
cxt.verify_mode = ssl.CERT_NONE

url = input('Enter JSON URL:')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.json'
fh = urllib.request.urlopen(url, context=cxt)
json_data = fh.read().decode()
try:
    info = json.loads(json_data)
except:
    info = None
sum = 0
for x in info['comments']:
    sum = sum + int(x['count'])
print(sum)